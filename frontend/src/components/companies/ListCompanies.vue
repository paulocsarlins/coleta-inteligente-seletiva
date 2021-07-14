<template>
  <div>
    <header-navbar></header-navbar>

    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          <a href="#!" class="breadcrumb">Início</a>
          <a href="#!" class="breadcrumb">Empresas</a>
        </div>
      </div>
    </nav>

    <div class="content card">
      <div class="row">
        <h2 class="animate__animated animate__fadeIn">
          <i class="far fa-building"></i>Empresas cadastradas

          <span><i class="fas fa-plus-circle"></i></span>
          </h2>

        <div class="col l12">
          <div class="card company-card animate__animated animate__fadeInUp animate__delay-1s" v-for="company of companies" v-bind:key="company">
            <h5><i class="fas fa-store"></i>{{company.name}}</h5>
            <p>{{company.cnpj}} &bull; {{company.segment}}</p>
            <span><i class="fas fa-map-marker-alt"></i>{{company.address}}</span>

            <div class="card-actions animate__animated animate__fadeIn animate__delay-2s">
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
import HeaderNavbar from '../template/HeaderNavbar.vue'

export default {
  components: { HeaderNavbar },
  name: 'list-companies',
  data(){
    return {
      companies: [
        { name: 'Instituto Federal de Pernambuco', segment: 'Educação', cnpj: '31.433.171/0001-38', address: 'Rua X, número 2, Palmares/PE' },
        { name: 'Coca-cola SA', segment: 'Indústria', cnpj: '81.795.080/0001-10', address: 'Rua Y, número 14, Recife/PE' },
        { name: 'Pão de Açúcar', segment: 'Alimentos', cnpj: '65.448.277/0001-27', address: 'Rua Z, número 28, Recife/PE' },
        { name: 'Parque da Jaqueira', segment: 'Lazer', cnpj: '88.975.277/0001-27', address: 'Rua da jaqueira, sem número, Recife/PE' },
        { name: 'Posto Shell 12', segment: 'Posto de gasolina', cnpj: '32.123.523/0008-17', address: 'Avenida Agamenon Magalhães, 886, Recife/PE' }
      ]
    }
  },
  created: function() {
    
  }
}
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
  background: rgba(0,0,0,0.005);
}

.content h2 {
  font-size: 1.7rem;
  color: #20962B;
}

.content h2 i {
  margin-right: 10px;
}

.company-card {
  padding: 10px 15px;
  color: #555;
}

.company-card h5 {
  font-size: 1.2rem;
  margin: 0;
}

.company-card i {
  margin-right: 5px;
}

.company-card span {
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
  color: #00A8E9;
  margin-right: 10px;
}

.card-actions .fa-trash-alt {
  color: #C0392B;
}

h2 span {
  float: right;
  cursor: pointer;
}
</style>
