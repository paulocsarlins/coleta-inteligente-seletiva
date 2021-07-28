<template>
  <div>
    <header-navbar />
    <div class="cadastro-form card">
      <div class="row">
        <form class="col s12">

          <div class="title-login">
            <a v-on:click="TelaLogin">LOGIN <i class="fas fa-angle-double-right"></i></a>
          </div>
          <div class="title-cadastro">
            <a>CADASTRE-SE</a>
          </div>

          <p class="blog-title">
            Crie sua conta informando os seus dados nos campos abaixo.
          </p>

          <div class="row no-margin-bottom">
            <div class="input-field col s12">
              <input id="nome" type="text" class="validate" v-model="nome" />
              <label for="nome"
                ><i class="fa fa-clipboard"></i> Informe seu nome
                completo</label
              >
            </div>
          </div>

          <div class="row no-margin-bottom">
            <div class="input-field col s12">
              <input id="email" type="email" class="validate" v-model="email" />
              <label for="email"
                ><i class="fa fa-envelope"></i> Informe seu e-mail</label
              >
            </div>
          </div>
          <div class="row no-margin-bottom">
            <div class="input-field col s12">
              <input
                id="password"
                type="password"
                class="validate"
                v-model="senha"
              />
              <label for="password"
                ><i class="fa fa-key"></i> Informe sua senha</label
              >
            </div>
          </div>
          <div class="row">
            <div class="input-field col s12">
              <input
                id="confirmar-senha"
                type="password"
                class="validate"
                v-model="confirmacaoSenha"
              />
              <label for="confirmar-senha"
                ><i class="fa fa-key"></i> Confirmação sua senha</label
              >
              <span v-if="senha != confirmacaoSenha" class="erro-senha"
                ><i class="fa fa-times"></i>As senhas informadas não são
                iguais!</span
              >
            </div>
          </div>
          <div class="row">
            <a
              v-on:click="cadastrar"
              class="waves-effect waves-light btn btn-large botao-cadastro"
              >CADASTRAR</a
            >
          </div>
          <div class="row">
            <p class="cancelar-cadastro" v-on:click="TelaHome">Cancelar Cadastro</p>
          </div>
          <div class="row">
            <p class="efetuar-login" v-on:click="TelaLogin">Deseja efetuar seu Login?</p>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNavbar from "./HeaderNavbar.vue";

export default {
  components: { HeaderNavbar },
  name: "Cadastro",

  data() {
    return {
      nome: "",
      email: "",
      senha: "",
      confirmacaoSenha: "",
    };
  },

  methods: {
    TelaLogin() {
      this.$router.push({ name: "Login" });
    },
     TelaHome() {
      this.$router.push({ name: "Home" });
    },

    cadastrar: function () {
      if (
        this.nome == "" ||
        this.email == "" ||
        this.senha == "" ||
        this.confirmacaoSenha == "" ||
        this.senha != this.confirmacaoSenha
      ) {
        alert("Preencha todos os campos com dados válidos!");
      } else {
        ({
          nome: this.nome,
          email: this.email,
          senha: this.senha,
          confirmacaoSenha: this.confirmacaoSenha,
        });
        this.$router.push({ name: "Login" });
        alert("Dados cadastrados com sucesso!");
        this.nome = "";
        this.email = "";
        this.senha = "";
        this.confirmacaoSenha = "";
      }
    },
  },
};
</script>

<style scoped>
.cadastro-form {
  border-radius: 50px 50px;
  width: 35vw;
  margin-left: 45vw;
  padding: 25px;
  background: #E5E5E5;
  margin-top: 2%;
}

.title-cadastro {
  text-align: left;
  font-size: 50px;
  font-weight: Red Rose;
  margin-top: 5px;
}

.title-login {
  text-align: right;
  font-size: 25px;
  font-weight: Red Rose;
  margin-top: 0px;
  text-decoration-line: underline;
  cursor: pointer;
}
.title-cadastro a,
.title-login a {
  color: #000000;
}
.title-login a:hover {
  border-radius: 6px;
  background: #87ceeb !important;
  color: white !important;
}
.blog-title {
  text-align: center;
  color: rgb(46, 41, 41);
  font-size: 16px;
  font-weight: bold;
  margin-top: 5px;
}

.botao-cadastro {
  width: 70%;
  border-radius: 150px;
  font-weight: bold;
  margin-left: 15%;
}

.botao-cadastro {
  background: white;
  color: #444444 !important;
  border: 1px solid #757575 !important;
  font-weight: bold;
}

.botao-cadastro:hover {
  background: #757575 !important;
  color: white !important;
}

.cancelar-cadastro {
  color: #1565c0;
  cursor: pointer;
  margin-bottom: 0;
  text-align: center;
}

.efetuar-login {
  color: #1565c0;
  cursor: pointer;
  margin-bottom: 0;
  text-align: center;
}

.no-margin-bottom,
.no-margin-bottom .input-field {
  margin-bottom: 0 !important;
}

.erro-senha {
  background: #e47f7f;
  border: 1px solid #c01515;
  font-weight: bold;
}
.erro-senha i {
  margin-right: 5px;
}
.row i {
  font-size: 20px;
}
</style>