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
          <li><a v-on:click="TelaHome">Início</a></li>
          <li><a href="badges.html">Denúncias</a></li>
          <li><a href="badges.html">Dicas</a></li>
          <li><a href="badges.html">Quem somos</a></li>
          <li><a href="collapsible.html">Perfil</a></li>
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
