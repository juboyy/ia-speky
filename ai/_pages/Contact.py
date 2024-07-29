st.header(":mailbox: Entre em contato comigo!")


contact_form = """
<form action="https://formsubmit.co/finess.org@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="true">
     <input type="text" name="name" placeholder="Seu nome" required>
     <input type="email" name="email" placeholder="Seu email" required>
     <textarea name="message" placeholder="Sua mensagem aqui"></textarea>
     <button type="submit">Enviar</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)
# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css(r"style/style.css")