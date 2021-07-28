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
          <li><router-link to="/">Início</router-link></li>
          <li><a v-on:click="TelaDenuncia">Denúncias</a></li>
          <li><a href="javascript:void(0);">Dicas</a></li>
          <li><router-link to="ListaEmpresas">Empresas</router-link></li>
          <li><a href="javascript:void(0);">Quem somos</a></li>
          <li><a href="javascript:void(0);">Perfil</a></li>
        </ul>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
  name: "header-navbar",

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
  },
};
</script>

<style>
nav.menu-superior {
  background: #197723;
}

nav .brand-logo {
  padding: 7px 32px;
}

nav .brand-logo img {
  height: 42px;
}
</style>
