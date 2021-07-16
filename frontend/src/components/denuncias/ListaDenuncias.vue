<template>
  <div>
    <header-navbar></header-navbar>

    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          <a href="#!" class="breadcrumb">Início</a>
          <a href="#!" class="breadcrumb">Denúncias</a>
        </div>
      </div>
    </nav>

    <div class="content card">
      <div class="row">
        <h2 class="animate__animated animate__fadeIn">
          <i class="fas fa-bullhorn"></i>Denúnicas cadastradas

          <span><i class="fas fa-plus-circle"></i></span>
          </h2>

        <div class="col l12">
          <div class="card company-card animate__animated animate__fadeInUp animate__delay-1s" v-for="denuncia of denuncias" v-bind:key="denuncia">
            <h5><i class="fas fa-map-marker-alt"></i>
            
            Endereço: {{denuncia.endereco}}
            <p>Número: {{denuncia.numero}}</p>
            <p>Bairro: {{denuncia.bairro}}</p>
            <p>Cidade: {{denuncia.cidade}}</p>
            
            </h5>
            <p>Denúncia: {{denuncia.descricao}}</p>
            

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
  name: 'lista-denuncias',
  data(){
    return {
      denuncias: [
        { endereco: 'Rua Primeiro de Maio', numero: '395', bairro: 'Santa Luzia', cidade: 'Palmares/PE', descricao:'Lixo na calçada' },
        { endereco: 'Rua Ivanildo Lins', numero: '1257', bairro: 'Santa Rosa', cidade: 'Palmares/PE', descricao:'Entulho de construção no meio da rua' },
        { endereco: 'Praça Santo Amaro', numero: '', bairro: 'Santo Amaro', cidade: 'Palmares/PE', descricao:'Lixo na praça' },
        { endereco: 'Travessa Tenente Everaldo', numero: '1365', bairro: 'Santo Onofre', cidade: 'Palmares/PE', descricao:'O lixo não é coletado há 12 dias' },
        { endereco: 'Travessa Luiza Pedroza', numero: '125', bairro: 'Coabe 2', cidade: 'Palmares/PE', descricao:'O carro da coleta não passa há 8 dias' },
        { endereco: 'Praça Paulo Paranhos', numero: '', bairro: 'Centro', cidade: 'Palmares/PE', descricao:'O lixo das lixeiras não está sendo recolhido' },
         
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
