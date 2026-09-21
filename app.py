import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="BikeCadastro PRO", page_icon="🚲", layout="wide", initial_sidebar_state="expanded")

ARQUIVO = "bicicletas.csv"
IMAGEM_HERO = "https://images.unsplash.com/photo-1571068316344-75bc76f77890?auto=format&fit=crop&w=1800&q=90"
IMAGEM_BIKE = "https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=1200&q=85"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap');
html,body,[class*="css"]{font-family:'Poppins',sans-serif}
.stApp{background:linear-gradient(135deg,#eef7f1 0%,#dcefe3 50%,#c9e3d2 100%)}
.block-container{max-width:1400px;padding-top:2rem;padding-bottom:3rem}
[data-testid="stSidebar"]{background:linear-gradient(180deg,#102b20,#1d4937);border-right:2px solid #49a66f}
[data-testid="stSidebar"] *{color:#fff!important}
.logo-title{font-size:28px;font-weight:800;color:#fff!important;margin-bottom:5px}.logo-subtitle{font-size:11px;font-weight:700;color:#bce7ca!important;letter-spacing:1px}
.page-title{font-size:38px;font-weight:800;color:#173b2a!important;margin-bottom:5px}.page-subtitle{font-size:17px;color:#466352!important;margin-bottom:30px}
.hero-container{position:relative;height:430px;width:100%;border-radius:28px;overflow:hidden;margin-bottom:35px;background-size:cover;background-position:center;box-shadow:0 15px 35px rgba(0,0,0,.22)}
.hero-overlay{position:absolute;inset:0;background:linear-gradient(90deg,rgba(9,34,24,.97),rgba(9,34,24,.82) 45%,rgba(9,34,24,.15))}
.hero-content{position:absolute;top:50%;left:7%;transform:translateY(-50%);max-width:600px}.hero-number{font-size:70px;font-weight:800;color:#72d79b!important;line-height:1}.hero-title{font-size:46px;font-weight:800;color:#fff!important;margin-top:12px;line-height:1.1}.hero-text{font-size:17px;color:#e4f5ea!important;margin-top:20px;line-height:1.7}.hero-badge{display:inline-block;margin-top:24px;padding:10px 22px;border-radius:30px;background:#2f9b61;color:#fff!important;font-size:14px;font-weight:700}
.info-card{background:#fff;border-radius:22px;padding:28px;min-height:170px;border:1px solid rgba(47,155,97,.25);box-shadow:0 10px 25px rgba(0,0,0,.08)}
.card-icon{font-size:32px}.card-number{font-size:34px;font-weight:800;color:#173b2a!important;margin-top:10px}.card-label{font-size:14px;font-weight:700;color:#587064!important;margin-top:5px}
.dark-card{background:linear-gradient(135deg,#123426,#20563f);border-radius:24px;padding:30px;box-shadow:0 12px 30px rgba(0,0,0,.16)}.dark-card h2{color:#fff!important;margin-top:0}.dark-card p{color:#e0f3e7!important;line-height:1.7}
[data-testid="stForm"]{background:rgba(255,255,255,.88);padding:30px;border-radius:25px;border:1px solid #a8d3b7;box-shadow:0 10px 30px rgba(0,0,0,.08)}
[data-testid="stWidgetLabel"],.stTextInput label,.stNumberInput label,.stSelectbox label,.stTextArea label{color:#173b2a!important;opacity:1!important;font-size:15px!important;font-weight:700!important}
.stTextInput input,.stNumberInput input,.stTextArea textarea{background:#fff!important;color:#18241d!important;-webkit-text-fill-color:#18241d!important;border:2px solid #72a888!important;border-radius:12px!important;font-size:16px!important}
[data-baseweb="select"]>div{background:#26342d!important;border:2px solid #72a888!important;border-radius:12px!important}[data-baseweb="select"]>div *{color:#fff!important;-webkit-text-fill-color:#fff!important}[data-baseweb="menu"],[data-baseweb="popover"],[role="option"]{background:#26342d!important;color:#fff!important}[role="option"]:hover{background:#2f8055!important}
.stButton>button,div[data-testid="stFormSubmitButton"]>button{background:linear-gradient(135deg,#23764a,#3caf6c)!important;color:#fff!important;border:none!important;border-radius:14px!important;min-height:54px;font-weight:700!important;box-shadow:0 8px 18px rgba(35,118,74,.25)}
.stButton>button:hover,div[data-testid="stFormSubmitButton"]>button:hover{background:linear-gradient(135deg,#195c39,#2e9258)!important;color:#fff!important;transform:translateY(-1px)}
[data-testid="stDataFrame"]{background:#fff;border-radius:18px;overflow:hidden;border:1px solid #a8d3b7}.footer{margin-top:50px;text-align:center;color:#466352!important;font-size:14px;font-weight:600}
@media(max-width:768px){.hero-container{height:500px}.hero-content{left:8%;right:8%}.hero-title{font-size:34px}.hero-number{font-size:55px}.page-title{font-size:30px}}
</style>
""", unsafe_allow_html=True)

def carregar_dados():
    colunas=["Marca","Modelo","Ano","Cor","Número de série","Aro","Tipo","Valor","Observações"]
    if os.path.exists(ARQUIVO):
        try:
            return pd.read_csv(ARQUIVO)
        except Exception:
            pass
    return pd.DataFrame(columns=colunas)

def salvar_dados(dados): dados.to_csv(ARQUIVO,index=False)

df=carregar_dados()
colunas=["Marca","Modelo","Ano","Cor","Número de série","Aro","Tipo","Valor","Observações"]
for c in colunas:
    if c not in df.columns: df[c]=""
df["Valor"]=pd.to_numeric(df["Valor"],errors="coerce").fillna(0)
df["Aro"]=pd.to_numeric(df["Aro"],errors="coerce").fillna(0)

st.sidebar.markdown('<div class="logo-title">🚲 BikeCadastro</div><div class="logo-subtitle">GESTÃO INTELIGENTE DE BICICLETAS</div>',unsafe_allow_html=True)
st.sidebar.markdown('<br>',unsafe_allow_html=True)
menu=st.sidebar.radio("NAVEGAÇÃO",["🏠 Dashboard","➕ Cadastrar Bicicleta","🚲 Bicicletas Cadastradas"])
st.sidebar.markdown('---'); st.sidebar.caption("BikeCadastro PRO • 2026")

if menu=="🏠 Dashboard":
    st.markdown(f'''<div class="hero-container" style="background-image:url('{IMAGEM_HERO}')"><div class="hero-overlay"></div><div class="hero-content"><div class="hero-number">01.</div><div class="hero-title">Suas bikes.<br>Seu controle.</div><div class="hero-text">Tenha todas as suas bicicletas organizadas em um único lugar.<br>Cadastre, consulte e acompanhe sua coleção de forma simples e profissional.</div><div class="hero-badge">🚲 GESTÃO INTELIGENTE</div></div></div>''',unsafe_allow_html=True)
    st.markdown('<div class="page-title">📊 Visão geral das suas bicicletas</div><div class="page-subtitle">Acompanhe sua coleção e mantenha tudo organizado.</div>',unsafe_allow_html=True)
    total=len(df); valor=df["Valor"].sum(); tipos=df["Tipo"].replace("","Não informado").nunique() if not df.empty else 0
    c1,c2,c3=st.columns(3)
    cards=[("🚲",total,"BICICLETAS CADASTRADAS"),("💰",f"R$ {valor:,.2f}","VALOR TOTAL DA COLEÇÃO"),("🛞",tipos,"TIPOS DE BICICLETA")]
    for col,(icon,num,label) in zip((c1,c2,c3),cards):
        with col: st.markdown(f'<div class="info-card"><div class="card-icon">{icon}</div><div class="card-number">{num}</div><div class="card-label">{label}</div></div>',unsafe_allow_html=True)
    st.markdown('<br>',unsafe_allow_html=True); a,b=st.columns([1.1,1])
    with a: st.markdown('<div class="dark-card"><h2>🚀 Controle profissional</h2><p>O BikeCadastro PRO permite manter todas as suas bicicletas organizadas em um único lugar.</p><p>Cadastre, consulte, pesquise e acompanhe as informações da sua coleção de maneira moderna e profissional.</p></div>',unsafe_allow_html=True)
    with b: st.image(IMAGEM_BIKE,use_container_width=True)

elif menu=="➕ Cadastrar Bicicleta":
    st.markdown('<div class="page-title">➕ Nova bicicleta</div><div class="page-subtitle">Adicione uma nova bicicleta ao seu BikeCadastro PRO.</div>',unsafe_allow_html=True)
    with st.form("cadastro_bicicleta",clear_on_submit=True):
        c1,c2=st.columns(2)
        with c1:
            marca=st.text_input("🏷️ Marca"); modelo=st.text_input("🚲 Modelo"); ano=st.number_input("📅 Ano",min_value=1900,max_value=2035,value=2024,step=1)
            cor=st.selectbox("🎨 Cor",["Preto","Branco","Azul","Vermelho","Cinza","Verde","Amarelo","Rosa","Roxo","Outro"])
            tipo=st.selectbox("🚲 Tipo",["Mountain Bike","Speed","Urbana","BMX","Elétrica","Infantil","Outra"])
        with c2:
            serie=st.text_input("🔢 Número de série"); aro=st.number_input("📏 Aro",min_value=12,max_value=36,value=29,step=1); valor=st.number_input("💰 Valor da Bicicleta",min_value=0.0,value=0.0,step=100.0); obs=st.text_area("📝 Observações")
        cadastrar=st.form_submit_button("💾 CADASTRAR BICICLETA")
    if cadastrar:
        if marca.strip() and modelo.strip() and serie.strip():
            nova=pd.DataFrame([{"Marca":marca.strip(),"Modelo":modelo.strip(),"Ano":int(ano),"Cor":cor,"Número de série":serie.strip().upper(),"Aro":int(aro),"Tipo":tipo,"Valor":float(valor),"Observações":obs.strip()}])
            df=pd.concat([df,nova],ignore_index=True); salvar_dados(df); st.success("🚲 Bicicleta cadastrada com sucesso!"); st.rerun()
        else: st.warning("⚠️ Preencha Marca, Modelo e Número de série.")

else:
    st.markdown('<div class="page-title">🚲 Minhas bicicletas</div><div class="page-subtitle">Consulte e pesquise todas as bicicletas cadastradas.</div>',unsafe_allow_html=True)
    if df.empty:
        st.markdown('<div class="dark-card"><h2>🚲 Nenhuma bicicleta cadastrada</h2><p>Sua coleção ainda está vazia. Cadastre sua primeira bicicleta para começar.</p></div>',unsafe_allow_html=True)
    else:
        busca=st.text_input("🔎 Pesquisar bicicleta",placeholder="Digite marca, modelo, número de série, tipo ou cor...")
        if busca:
            mascara=df.astype(str).apply(lambda c:c.str.contains(busca,case=False,na=False)).any(axis=1); filtrado=df[mascara]
        else: filtrado=df
        st.dataframe(filtrado,use_container_width=True,hide_index=True)
        st.markdown('<br>',unsafe_allow_html=True)
        idx=st.selectbox("🗑️ Selecione uma bicicleta para excluir",options=df.index.tolist(),format_func=lambda i:f"{df.loc[i,'Marca']} {df.loc[i,'Modelo']} - Série {df.loc[i,'Número de série']}")
        if st.button("🗑️ EXCLUIR BICICLETA"):
            df=df.drop(idx).reset_index(drop=True); salvar_dados(df); st.success("🚲 Bicicleta excluída com sucesso!"); st.rerun()

st.markdown('<div class="footer">🚲 BikeCadastro PRO<br>Cadastro e gestão de bicicletas</div>',unsafe_allow_html=True)
