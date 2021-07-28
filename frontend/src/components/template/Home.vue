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
          <h3 class="title2">
            Mude seus hábitos e sua formar de descartar seu lixo!
          </h3>

          <form class="for-login-cadastro">
            <h5 class="title3">Faça parte dessa mudança!</h5>
            <a
              v-on:click="TelaLogin"
              class="waves-effect waves-light btn btn-large botao-login"
              >LOGIN</a
            >
            <h6 class="title3">OU</h6>
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
body {
  zoom: 0.8;
}
.container {
  width: 100%;
  display: flex;

  max-width: 100%;
  margin: 0;
  padding: 0;
}

.img-home {
  width: 50%;
  margin-top: 1%;
}

.title1 {
  text-align: center;
  font-size: 4rem;
  font-weight: bold;
  text-shadow: 0.1em 0.1em 0.2em black;
}
.title2 {
  text-align: center;
  font-size: 3rem;
  text-shadow: 0 0 0.2em;
}
.title3 {
  font-weight: bold;
}
.form-login-cadastro {
  margin-left: -1vw;
  text-align: center;
  width: 50%;
  background: white;
  border-radius: 50px;
}
.for-login-cadastro {
  text-align: center;
  padding: 15px;
  margin-left: 25%;
  margin-right: 15vw;
  background: #c4c4c4;
  border-radius: 50px;
  margin-top: 13%;
}

.botao-cadastrar,
.botao-login {
  width: 50%;
  margin-left: 0%;
  margin-right: 0%;
  border-radius: 150px;
  font-weight: bold;
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
