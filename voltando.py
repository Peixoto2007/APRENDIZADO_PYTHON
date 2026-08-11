from ollama import chat
import pandas as pd
import json
import re


arquivo = pd.read_excel('planilha.xlsx', sheet_name=None)

planilha = arquivo['Sheet1']
banco = arquivo['banco']


planilha.columns = planilha.columns.str.strip().str.lower()
banco.columns = banco.columns.str.strip().str.lower()


planilha['cadastro sugerido'] = planilha.get('cadastro sugerido', "").astype(str)
planilha['status'] = planilha.get('status', "").astype(str)
planilha['ncm sugerido'] = planilha.get('ncm sugerido', "").astype(str)


banco_materiais = set(
    banco['material']
    .astype(str)
    .str.lower()
    .str.replace(r'[^\w\s]', '', regex=True)
    .str.strip()
)


for i, descricao in enumerate(planilha['material']):

    if pd.isna(descricao):
        continue

    descricao_limpa = re.sub(r'[^\w\s]', '', str(descricao).lower()).strip()

    # ✅ já existe
    if descricao_limpa in banco_materiais:
        resultado = descricao_limpa.upper()
        status = "JA_EXISTE"
        ncm = ""

    # 🤖 IA
    else:
        prompt = f"""
Você é um sistema automático de cadastro industrial.

Responda APENAS JSON puro (sem ```).

ITEM:
{descricao}

FORMATO:
{{
  "status": "JA_EXISTE ou NOVO",
  "descricao": "NOME",
  "ncm": "00000000"
}}
"""

        response = chat(
            model='deepseek-v3.2:cloud',
            messages=[{'role': 'user', 'content': prompt}]
        )

        conteudo = response.message.content.strip()

        
        match = re.search(r'\{.*?\}', conteudo, re.DOTALL)

        if match:
            json_str = match.group(0)
        else:
            json_str = ""

        try:
            dados = json.loads(json_str)

            resultado = dados.get("descricao", "")
            status = dados.get("status", "")
            ncm = dados.get("ncm", "")

        except:
            print("Erro ao interpretar:", conteudo)

            resultado = str(descricao).upper()
            status = "ERRO"
            ncm = ""

    
    planilha.loc[i, 'cadastro sugerido'] = str(resultado)
    planilha.loc[i, 'status'] = str(status)
    planilha.loc[i, 'ncm sugerido'] = str(ncm)


with pd.ExcelWriter('planilha.xlsx', engine='openpyxl') as writer:
    planilha.to_excel(writer, sheet_name='Sheet1', index=False)
    banco.to_excel(writer, sheet_name='banco', index=False)

print("Finalizado.")