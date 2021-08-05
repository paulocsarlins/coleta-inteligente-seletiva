<template>
  <div>
    <nav class="menu-superior animate__animated animate__fadeInDown">
      <div class="nav-wrapper">
        <a
          href="#"
          class="
            brand-logo
            animate__animated animate__heartBeat animate__delay-1s
          "
          ><img src="@/assets/logo.png"
        /></a>
        <ul id="nav-mobile" class="right hide-on-med-and-down">
          <li><router-link to="/HomeUser">Início</router-link></li>
          <li><a v-on:click="TelaDenuncia">Denúncias</a></li>
          <li><a v-on:click="TelaPaginaBranco">Dicas</a></li>
          <li><a v-on:click="TelaPaginaBranco">Quem somos</a></li>
          <li><a v-on:click="TelaPaginaBranco"><i class="far fa-user"></i></a></li>
          <li><router-link to="/"><i class="fas fa-sign-out-alt"></i> </router-link></li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "user-header-navbar",

  data() {
    return {};
  },

  methods: {
    TelaHome() {
      this.$router.push({ name: "Home" });
    },
    TelaDenuncia() {
      this.$router.push({ name: "ListaDenuncias" });
    },
    TelaPontosDeColeta() {
      this.$router.push({ name: "PontosDeColeta" });
    },
     TelaPaginaBranco() {
      this.$router.push({ name: "UserPaginaBranco" });
    },
  },
};
</script>

<style>
nav.menu-superior {
  background: #2e7d32;
}

nav .brand-logo {
  padding: 7px 32px;
}

nav .brand-logo img {
  height: 42px;
}
</style>
