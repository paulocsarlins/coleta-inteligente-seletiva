<template>
  <div>
    <header-navbar />

    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          <a href="#!" class="breadcrumb">Início</a>
        </div>
      </div>
    </nav>
    <div class="container">
      <img class="img-home" src="https://i.ibb.co/cLXgBjD/cil.png" alt="" />
      <form class="form-login-cadastro">
        <div class="row">
          <h1 class="title1">Transforme o mundo ao seu redor</h1>
          <form class="login-cadastro">
            <a
              v-on:click="TelaLogin"
              class="waves-effect waves-light btn btn-large botao-login"
              >LOGIN</a
            >
            <h4 class="title">ou</h4>
            <a
              v-on:click="TelaCadastro"
              class="waves-effect waves-light btn btn-large botao-cadastrar"
              >CADASTRAR</a
            >
          </form>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import HeaderNavbar from "./HeaderNavbar.vue";

export default {
  components: { HeaderNavbar },
  name: "home",
  data() {
    return {};
  },
  methods: {
    TelaLogin() {
      this.$router.push({ name: "Login" });
    },
    TelaCadastro() {
      this.$router.push({ name: "Cadastro" });
    },
  },  
  created: function () {},
};

</script>

<style>
.container {
  display: flex;
  align-items: center;
}

.img-home {
  width: 1000px;
  height: 1000px;
  margin-top: 1%;
  margin-left: -15%;
}
.title1 {
  margin-top: -20%;
  text-align: center;
}
.form-login-cadastro {
  width: 40vw;
  margin-left: -1vw;
  text-align: center;
  padding: 203px;
  background: white;
  border-radius: 50px;
  margin-top: 1%;
}
.login-cadastro {
  width: 25vw;
  margin-left: -1vw;
  text-align: center;
  padding: 203px;
  background: #C4C4C4;
  border-radius: 50px;
  margin-top: 50%;
}

.botao-cadastrar,
.botao-login {
  width: 90%;
  border-radius: 150px;
  font-weight: bold;
  margin-left: 15%;
}

.botao-cadastrar,
.botao-login {
  background: white;
  color: #444444 !important;
  border: 1px solid #757575 !important;
  font-weight: bold;
}

.botao-cadastrar:hover,
.botao-login:hover {
  background: #757575 !important;
  color: white !important;
}
</style>
