<template>
  <div>
    <footer class="page-footer green darken-3">
      <div class="container">
        <div class="row">
          <center>
            <div class="col l7 s12">
              <a
                href="#"
                class="
                  brand-logo
                  animate__animated animate__heartBeat animate__delay-1s
                "
                ><img src="@/assets/logo.png"
              /></a>
              <h5 class="white-text">Nosso Projeto</h5>
              <h6 class="grey-text text-lighten-4">
                A Coleta Inteligente Seletiva é uma aplicação web, desenvolvido
                para acompanhar e incentivar o descarte correto de materiais
                poluentes, como também denunciar quando isso não é feito. Tendo
                como principal um trabalho com a comunidade.
              </h6>
            </div>
          </center>

          <center>
            <div class="col l5 s12">
              <h5 class="white-text">Acesso rápido</h5>
              <ul>
                <li>
                  <a
                    class="texto grey-text text-lighten-3"
                    href="#!"
                    v-on:click="TelaHome"
                    ><i class="fas fa-home"></i> Início</a
                  ><router-link to="/"></router-link>
                </li>
                <li>
                  <a
                    href="#!"
                    class="texto grey-text text-lighten-3"
                    v-on:click="TelaPaginaBranco"
                    ><i class="fas fa-chalkboard-teacher"></i> Dicas</a
                  >
                </li>
                <li>
                  <a
                    href="#!"
                    class="texto grey-text text-lighten-3"
                    v-on:click="TelaPaginaBranco"
                    ><i class="fas fa-users"></i> Quem somos</a
                  >
                </li>
              </ul>
            </div>
          </center>
        </div>
      </div>
      <div class="footer-copyright">
        <div class="container">© 2021 Todos os direitos reservados.</div>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: "footer-rodape",

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
      this.$router.push({ name: "PaginaBranco" });
    },
  },
};
</script>

<style>
.page-foote {
  background: #197723;
}
.page-footer container {
  margin-top: 100%;
}

.brand-logo {
  padding: 7px 32px;
}

.brand-logo img {
  height: 60px;
}
.item {
  align-items: center;
}

body {
  display: flex;
  min-height: 100vh;
  flex-direction: column;
}

main {
  flex: 1 0 auto;
}
</style>
