<template>
  <div>
    <header-navbar />

    <div class="login-form card">
      <div v-if="exibirMensagemErro" class="alert alert-danger">
        <strong>Erro!</strong> E-mail e/ou senha inválido(s).
      </div>

      <div class="row">
        <form class="col s12">
          <div class="title-cadastro">
            <a v-on:click="TelaCadastro"
              >CADASTRE-SE <i class="fas fa-angle-double-right"></i
            ></a>
          </div>
          <div class="title-login">
            <a v-on:click="TelaLogin">LOGIN</a>
          </div>
          <div class="row no-margin-bottom">
            <div class="input-field col s12">
              <input id="email" type="email" class="validate" v-model="email" />
              <label for="email"><i class="fa fa-envelope"></i> E-mail</label>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input
                id="password"
                type="password"
                class="validate"
                v-model="senha"
              />
              <label for="password"><i class="fa fa-key"></i> Senha</label>
            </div>
          </div>
          <div class="row">
            <a
              v-on:click="login"
              class="waves-effect waves-light btn btn-large botao-login"
              >ENTRAR</a
            >
          </div>
          <div class="row">
            <p class="cancelar-login" v-on:click="TelaHome">Cancelar Login</p>
          </div>
          <div class="row">
            <p class="esqueceu-a-senha">Esqueceu a senha?</p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNavbar from '../template/HeaderNavbar.vue';

export default {
  components: { HeaderNavbar },
  name: "Login",

  methods: {
    TelaHome() {
      this.$router.push({ name: "Home" });
    },
    TelaCadastro() {
      this.$router.push({ name: "Cadastro" });
    },
    login() {
      if (this.email == "teste@gmail.com" && this.senha == "ipi203") {
        this.$router.push({ name: "HomeUser" });
      } else {
        (this.email == "" && this.senha == "") ||
          ((this.email == "") != this.senha) == "";
        alert("Preencha os campos para fazer login!");
      }
    },
  },
};
</script>

<style scoped>
.login-form {
  width: 38vw;
  margin-left: 45vw;
  text-align: center;
  padding: 25px;
  background: #e5e5e5;
  border-radius: 50px;
  margin-top: 2%;
}
.title-login {
  text-align: left;
  font-size: 50px;
  font-weight: Red Rose;
  margin-top: 0px;
}

.title-cadastro {
  text-align: right;
  font-size: 25px;
  font-weight: Red Rose;
  margin-top: 5px;
  text-decoration-line: underline;
  cursor: pointer;
}
.title-cadastro a,
.title-login a {
  color: #000000;
}
.title-cadastro a:hover {
  border-radius: 6px;
  background: #87ceeb !important;
  color: white !important;
}
.blog-title {
  margin-left: 150vw;
}

.botao-login {
  width: 70%;
  border-radius: 150px;
  font-weight: bold;
  margin-left: 3%;
}

.botao-login {
  background: white;
  color: #444444 !important;
  border: 1px solid #757575 !important;
  font-weight: bold;
}

.botao-login:hover {
  background: #757575 !important;
  color: white !important;
}
.cancelar-login {
  color: #1565c0;
  cursor: pointer;
  margin-bottom: 0;
  text-align: center;
}

.esqueceu-a-senha {
  color: #1565c0;
  cursor: pointer;
  margin-bottom: 0;
  text-align: center;
}

.no-margin-bottom,
.no-margin-bottom .input-field {
  margin-bottom: 0 !important;
}

.alert {
  position: relative;
  padding: 0.75rem 0.75rem;
  border: 1px solid transparent;
  border-radius: 0.25rem;
  text-align: center;
  margin-top: 5px;
}

.alert-danger {
  color: #1d1c72;
  background-color: #a1bbe7;
  border-color: #6a89bf;
}

.botao-novo-usuario {
  background: white;
  color: #1565c0 !important;
  border: 1px solid #1565c0 !important;
  font-weight: bold;
}

.botao-novo-usuario:hover {
  background: #1565c0 !important;
  color: white !important;
}
.row i {
  font-size: 20px;
}
</style>
