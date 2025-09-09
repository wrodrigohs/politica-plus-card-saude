import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Política de Privacidade - Plus Card Saúde",
    page_icon="https://pluscardsaude.com.br/wp-content/uploads/2025/06/cropped-LOGO-01-32x32.png",
    layout="wide"
)

# Estilos CSS personalizados para replicar a aparência da página original
st.markdown("""
<style>
    /* Estilos Gerais */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    h1, h2, h3 {
        color: #194b85;
    }
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 15px;
    }
    h2 {
        font-size: 1.75rem;
        font-weight: 600;
        margin-top: 40px;
        margin-bottom: 20px;
        padding-bottom: 10px;
        border-bottom: 2px solid #e9ecef;
    }
    h3 {
        color: #333;
        font-size: 1.2rem;
        font-weight: 500;
        margin: 25px 0 15px 0;
    }
    p, li {
        color: #666;
        line-height: 1.7;
        margin-bottom: 15px;
        font-size: 1.1rem;
    }
    ul {
        margin-left: 40px;
        margin-bottom: 20px;
    }

    /* Cabeçalho */
    .privacy-policy-header {
        background: linear-gradient(135deg, #194b85 0%, #0050a0 100%);
        color: white;
        padding: 60px 20px;
        text-align: center;
        border-radius: 8px;
        margin-bottom: 40px;
    }
    .privacy-policy-header h1 {
        color: white;
    }
    .privacy-policy-header p {
        font-size: 1.2rem;
        opacity: 0.9;
        max-width: 600px;
        margin: 0 auto;
        color: white;
    }

    /* Seções */
    .privacy-section {
        margin-bottom: 30px;
    }

    /* Contato e Rodapé */
    .contact-info {
        background: #f0f7ff;
        border-left: 5px solid #194b85;
        padding: 25px;
        border-radius: 8px;
        margin-top: 40px;
    }
    .last-updated {
        text-align: center;
        padding: 30px 0;
        background: #f8f9fa;
        border-top: 1px solid #e9ecef;
        color: #666;
        font-weight: 500;
        margin-top: 40px;
        border-radius: 8px;
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        color: #888;
    }
</style>
""", unsafe_allow_html=True)

# --- Cabeçalho ---
st.markdown("""
<div class="privacy-policy-header">
    <h1>Política de Privacidade</h1>
    <p>Protegemos seus dados pessoais de acordo com a Lei Geral de Proteção de Dados (LGPD)</p>
</div>
""", unsafe_allow_html=True)

# --- Conteúdo da Política de Privacidade ---
st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 1. INTRODUÇÃO")
st.write("**1.1** Esta Política de Privacidade (\"Política\") descreve como a Plus Card Saúde trata os Dados Pessoais coletados por meio do Aplicativo, em conformidade com a Lei nº 13.709/2018 – Lei Geral de Proteção de Dados Pessoais (\"LGPD\").")
st.write("**1.2** Ao utilizar o Aplicativo, o Usuário manifesta ciência e concordância com as práticas aqui descritas.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 2. DADOS COLETADOS")
st.write("**2.1** Dados cadastrais: nome, CPF, data de nascimento, endereço, telefone, e-mail.")
st.write("**2.2** Dados de beneficiários/dependentes.")
st.write("**2.3** Dados sobre saúde (ex.: CID, prescrições, histórico de atendimento) necessários para agendamento e acompanhamento de casos.")
st.write("**2.4** Dados de uso: logs de acesso, IP, modelo do dispositivo, sistema operacional.")
st.write("**2.5** Cookies e tecnologias similares poderão ser empregadas para aprimorar a experiência de navegação.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 3. FINALIDADES")
st.write("**3.1** Prestação dos serviços de agendamento, histórico clínico, cartão virtual e telemedicina.")
st.write("**3.2** Execução de contrato com o Usuário (art. 7º, V, LGPD).")
st.write("**3.3** Cumprimento de obrigações legais/regulatórias (art. 7º, II, LGPD).")
st.write("**3.4** Proteção da saúde, em procedimento realizado por profissionais ou serviços de saúde (art. 11, II, \"f\", LGPD).")
st.write("**3.5** Exercício regular de direitos em processos judiciais ou administrativos.")
st.write("**3.6** Envio de comunicações institucionais ou ofertas, mediante consentimento (art. 7º, I).")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 4. BASES LEGAIS")
st.write("**4.1** A Plus Card Saúde utiliza as hipóteses legais dos arts. 7º e 11 da LGPD para legitimar o tratamento de Dados Pessoais e Dados Sensíveis.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 5. COMPARTILHAMENTO")
st.write("**5.1** Dados poderão ser compartilhados com:")
st.markdown("""
<ul>
    <li><strong>(a)</strong> Clínicas, hospitais, laboratórios e médicos credenciados, para prestação do atendimento;</li>
    <li><strong>(b)</strong> Prestadores de serviços de TI e nuvem, sob cláusulas de confidencialidade;</li>
    <li><strong>(c)</strong> Autoridades governamentais, mediante obrigação legal ou ordem judicial.</li>
</ul>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 6. TRANSFERÊNCIA INTERNACIONAL")
st.write("**6.1** Caso seja necessário armazenar dados em servidores fora do Brasil, a Plus Card Saúde adotará medidas para assegurar nível de proteção adequado, conforme arts. 33 e 34 da LGPD.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 7. ARMAZENAMENTO E RETENÇÃO")
st.write("**7.1** Dados são armazenados em ambiente seguro e controlado pelo tempo necessário às finalidades ou conforme exigido por lei.")
st.write("**7.2** Decorrido o prazo legal, dados serão eliminados ou anonimizados.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 8. DIREITOS DO TITULAR")
st.write("**8.1** O Usuário pode solicitar:")
st.markdown("""
<ul>
    <li><strong>(a)</strong> confirmação da existência de tratamento;</li>
    <li><strong>(b)</strong> acesso;</li>
    <li><strong>(c)</strong> correção;</li>
    <li><strong>(d)</strong> anonimização, bloqueio ou eliminação;</li>
    <li><strong>(e)</strong> portabilidade;</li>
    <li><strong>(f)</strong> informação sobre compartilhamento;</li>
    <li><strong>(g)</strong> revogação do consentimento, nos termos dos arts. 18 e 8º da LGPD.</li>
</ul>
""", unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 9. SEGURANÇA")
st.write("**9.1** São adotadas medidas técnicas e administrativas para proteger Dados Pessoais contra acessos não autorizados, incluindo criptografia, controle de acesso e registro de logs.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 10. COOKIES E TECNOLOGIAS")
st.write("**10.1** O Aplicativo pode utilizar cookies ou tecnologias equivalentes para autenticação, segurança e personalização de conteúdo. O Usuário poderá gerenciar tais tecnologias em seu dispositivo.")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="privacy-section">', unsafe_allow_html=True)
st.markdown("## 11. ATUALIZAÇÃO DA POLÍTICA")
st.write("**11.1** A presente Política poderá ser alterada. Versões atualizadas serão disponibilizadas no Aplicativo e entrarão em vigor na data da publicação.")
st.markdown('</div>', unsafe_allow_html=True)

# --- Informações de Contato ---
st.markdown('<div class="contact-info">', unsafe_allow_html=True)
st.markdown("## 12. CONTATO")
st.write("Dúvidas sobre esta Política ou sobre o tratamento de dados podem ser encaminhadas para:")
st.write("📧 **E-mail:** adm@pluscardsaude.com.br")
st.write("📍 **Endereço:** Rua Sete de Setembro, 2080, Sala 03, Centro, Campo Grande/MS")
st.write("📞 **Telefone:** (67) 9 9887-0780 - (67) 3253-6121")
st.markdown('</div>', unsafe_allow_html=True)

# --- Data da Última Atualização ---
st.markdown("""
<div class="last-updated">
    <p><strong>Atualizada em: 24 de julho de 2025</strong></p>
</div>
""", unsafe_allow_html=True)


# --- Rodapé ---
st.markdown("""
<div class="footer">
    <p>Copyright © Plus Card Saúde - Todos os Direitos Reservados</p>
</div>
""", unsafe_allow_html=True)