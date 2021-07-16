<template>
  <div>
    <header-navbar></header-navbar>

    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          <a href="#!" class="breadcrumb">Início</a>
          <a href="#!" class="breadcrumb">Pontos de Coleta</a>
        </div>
      </div>
    </nav>

    <div class="content card">
      <div class="row">
        <h2 class="animate__animated animate__fadeIn">
          <i class="fas fa-map-marked-alt"></i>Pontos de Coleta

          <span><i class="fas fa-plus-circle"></i></span>
        </h2>

        <div class="col l12">
          <div
            class="
              card
              pontoColeta-card
              animate__animated animate__fadeInUp animate__delay-1s
            "
            v-for="pontoColeta of pontosColeta"
            v-bind:key="pontoColeta"
          >
            <h5><i class="fas fa-user"></i>{{ pontoColeta.nome }}</h5>

            <p>
              <i class="fas fa-phone-alt"></i>
              {{ pontoColeta.telefone }}
            </p>

            <span>
              <i class="fas fa-map-marker-alt"></i
              >{{ pontoColeta.endereco }}</span
            >

            <p>
              <i class="fas fa-recycle"></i>
              {{ pontoColeta.materialColeta }} &bull;
              {{ pontoColeta.tipoMaterial }}
            </p>

            <div
              class="
                card-actions
                animate__animated animate__fadeIn animate__delay-2s
              "
            >
              <span><i class="far fa-edit"></i></span>
              <span><i class="far fa-trash-alt"></i></span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import HeaderNavbar from "../template/HeaderNavbar.vue";

export default {
  components: { HeaderNavbar },
  name: "pontos-de-coleta",
  data() {
    return {
      pontosColeta: [
        {
          nome: "Jefferson Henrique",
          telefone: "081 996693251",
          endereco: "Rua X, número 2, Palmares/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Papel, Vidro e Plástico",
        },
        {
          nome: "César Lins",
          telefone: "087 958631254",
          endereco: "Rua Y, número 14, Recife/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Vidro",
        },
        {
          nome: "Paulo Jóse",
          telefone: "088 932568744",
          endereco: "Rua Z, número 28, Recife/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Metal e Vidro",
        },
        {
          nome: "Francievellyn Larissa",
          telefone: "085 932157896",
          endereco: "Rua da jaqueira, sem número, Recife/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Vidro e Plástico",
        },
        {
          nome: "Victor Lira",
          telefone: "086 932158647",
          endereco: "Avenida Agamenon Magalhães, 886, Recife/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Plástico",
        },
        {
          nome: "Heitor Gabriel",
          telefone: "082 978546321",
          endereco: "Avenida Onze de Julho, 886, Recife/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Metal",
        },
        {
          nome: "Mariane Silva",
          telefone: "087 978596521",
          endereco: "Rua 12 de Abril, 987, Maraial/PE",
          materialColeta: "Marial para recolhimento:",
          tipoMaterial: "Papel",
        },
      ],
    };
  },
  created: function () {},
};
</script>

<style>
.menu-breadcrumb {
  background: #363636;
  padding-left: 20px;
}

.content {
  width: 70%;
  margin-left: 15%;
  padding: 1px 32px;
  margin-top: 20px;
  background: rgba(0, 0, 0, 0.005);
}

.content h2 {
  font-size: 1.7rem;
  color: #20962b;
}

.content h2 i {
  margin-right: 10px;
}

.pontoColeta-card {
  padding: 10px 15px;
  color: #555;
}

.pontoColeta-card h5 {
  font-size: 1.2rem;
  margin: 0;
}

.pontoColeta-card i {
  margin-right: 5px;
}

.pontoColeta-card span {
  color: #9a9a9a;
  font-size: 0.8rem;
}

.card-actions {
  position: absolute;
  right: 50px;
  top: 30%;
}

.card-actions span {
  cursor: pointer;
  font-size: 1.7rem;
}

.card-actions .fa-edit {
  color: #00a8e9;
  margin-right: 10px;
}

.card-actions .fa-trash-alt {
  color: #c0392b;
}

h2 span {
  float: right;
  cursor: pointer;
}
</style>
