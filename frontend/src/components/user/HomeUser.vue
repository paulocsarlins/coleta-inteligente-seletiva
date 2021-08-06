<template>
  <div>
    <user-header-navbar/>
    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          <a href="#!" class="breadcrumb" >Início</a>
        </div>
      </div>
    </nav>
    <div class="container">
      <img class="img-home" src="https://i.ibb.co/cLXgBjD/cil.png" alt="" />
      <form class="form-user">
        <div class="row">
          <h1 class="title1">Seja bem-vindo! </h1>
          <h3 class="title2">
            Que bom te ter na família, faremos uma grande mudança.
          </h3>

          <a
            v-on:click="TelaPontosDeColeta"
            class="waves-effect waves-light btn btn-large botao-coleta"
            ><i class="fas fa-map-marked-alt"></i> Pontos de Coleta</a
          >

          <a
            v-on:click="TelaDenuncia"
            class="waves-effect waves-light btn btn-large botao-denuncia"
            ><i class="fas fa-clipboard-list"></i> Denúncias</a
          >
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import UserHeaderNavbar from '../user/UserHeaderNavbar.vue';
export default {
  components: { UserHeaderNavbar },
  name: "home-user",
  data() {
    return {};
  },
  methods: {
    TelaDenuncia() {
      this.$router.push({ name: "ListaDenuncias" });
    },
    TelaPontosDeColeta() {
      this.$router.push({ name: "PontosDeColeta" });
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
.form-user {
  margin-left: -1vw;
  text-align: center;
  width: 50%;
  background: white;
  border-radius: 50px;
}

.botao-coleta,
.botao-denuncia {
  width: 50%;
  margin-left: 0%;
  margin-right: 1%;
  border-radius: 150px;
  font-weight: bold;
  margin-top: 5%;
  font-size: 2rem;
}

.botao-coleta,
.botao-denuncia {
  background: white;
  color: #444444 !important;
  border: 1px solid #757575 !important;
  font-weight: bold;
}

.botao-coleta:hover,
.botao-denuncia:hover {
  background: #757575 !important;
  color: white !important;
}
</style>
