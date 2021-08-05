<template>
  <div>
    <user-header-navbar/>
    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          <a href="#!" class="breadcrumb" v-on:click="HomeUser">Início</a>
          <a href="#!" class="breadcrumb">Denúncias</a>
          <a href="#!" class="breadcrumb">Lista de denúncias</a>
        </div>
      </div>
    </nav>

    <div class="content card">
      <div class="row">
        <h2 class="animate__animated animate__fadeIn">
          <i class="fas fa-bullhorn"></i>Denúnicas cadastradas

          <span><i class="fas fa-plus-circle" v-on:click="TelaCadastroDenuncias"></i></span>
          </h2>

        <div class="col l12">
          <div class="card company-card animate__animated animate__fadeInUp animate__delay-1s" v-for="denuncia of denuncias" v-bind:key="denuncia">
            <h5><i class="fas fa-map-marker-alt"></i>
            
            <a v-if="!denuncia.editar">Endereço: {{denuncia.endereco}}</a> 
            <p> <input v-if="denuncia.editar" type="text" v-model="denuncia.endereco"> </p>
            
            <p v-if="!denuncia.editar">Número: {{denuncia.numero}}</p> 
            <p> <input v-if="denuncia.editar" type="text" v-model="denuncia.numero"> </p>

            <p v-if="!denuncia.editar">Bairro: {{denuncia.bairro}}</p> 
            <p> <input v-if="denuncia.editar" type="text" v-model="denuncia.bairro"> </p>
            
            <p v-if="!denuncia.editar">Cidade: {{denuncia.cidade}}</p> 
            <p> <input v-if="denuncia.editar" type="text" v-model="denuncia.cidade"> </p>
            
            </h5>
            
            <p v-if="!denuncia.editar">Denúncia: {{denuncia.descricao}}</p> 
            <p> <input v-if="denuncia.editar" type="text" v-model="denuncia.descricao"> </p>

            <div class="card-actions animate__animated animate__fadeIn animate__delay-2s">
              
              <span v-if="!denuncia.editar" v-on:click="editeDenuncia(denuncia)"><i class="far fa-edit"></i></span>
              <span v-if="!denuncia.editar" v-on:click="deleteDenuncia(denuncia)"><i class="far fa-trash-alt"></i></span>

            </div>
                    
            <div class="btn-confirma-cancela">
              <span v-on:click="updateDenuncia(denuncia)" v-if="denuncia.editar" class="confirm-button"><i class="far fa-check-circle"></i></span>
              <span v-on:click="cancelEdit(denuncia)" v-if="denuncia.editar" class="remove-button"><i class="far fa-times-circle"></i></span>
            </div>

          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import UserHeaderNavbar from '../user/UserHeaderNavbar.vue';
export default {
  components: { UserHeaderNavbar },
  name: 'lista-denuncias',
  data(){
    return {
      denuncias: [
     /*   { id: 1 , endereco: 'Rua Primeiro de Maio', numero: '395', bairro: 'Santa Luzia', cidade: 'Palmares/PE', descricao:'Lixo na calçada' },
        { id: 2 , endereco: 'Rua Ivanildo Lins', numero: '1257', bairro: 'Santa Rosa', cidade: 'Palmares/PE', descricao:'Entulho de construção no meio da rua' },
        { id: 3 , endereco: 'Praça Santo Amaro', numero: '', bairro: 'Santo Amaro', cidade: 'Palmares/PE', descricao:'Lixo na praça' },
        { id: 4 , endereco: 'Travessa Tenente Everaldo', numero: '1365', bairro: 'Santo Onofre', cidade: 'Palmares/PE', descricao:'O lixo não é coletado há 12 dias' },
        { id: 5 , endereco: 'Travessa Luiza Pedroza', numero: '125', bairro: 'Coabe 2', cidade: 'Palmares/PE', descricao:'O carro da coleta não passa há 8 dias' },
        { id: 6 , endereco: 'Praça Paulo Paranhos', numero: '', bairro: 'Centro', cidade: 'Palmares/PE', descricao:'O lixo das lixeiras não está sendo recolhido' },
        */
      ]
    }
  },

  created: function() {
    this.loadDenuncias();
  },

  methods: {
    TelaCadastroDenuncias() {
      this.$router.push({ name: "CadastroDenuncias" });
    },
    TelaHomeUser() {
      this.$router.push({ name: "HomeUser" });
    },

    loadDenuncias() {
      axios.get('http://localhost:8000/api/getdenuncias')
        .then(response => {
          this.denuncias = response.data.denuncias;
        }).catch(error => console.log(error));
    },

    deleteDenuncia(denuncia) {
      axios.delete('http://localhost:8000/api/deletedenuncia/' + denuncia.id)
        .then(() => { 
          alert('Denúncia removida com sucesso!'); 
          this.loadDenuncias();
        }).catch(error => console.log(error));
    },

    editeDenuncia(denuncia) {
      denuncia.editar = true;
    },

    updateDenuncia(denuncia) {
      axios.put('http://localhost:8000/api/getdenuncias' + denuncia.id)
      .then(() => {
        alert('Denúncia editada com sucesso!');
        denuncia.editar = false;
      }).catch(error => console.log(error));
        denuncia.editar = false;

    },

    cancelEdit(denuncia) {
      denuncia.editar = false;
    }
    
  },

  
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

p {
    margin-left: 24px;
}

.fa-check-circle{
  color: green;
}
.fa-times-circle{
  color: red;
}

input {
  width: 450px!important;
}

.fa-check-circle, .fa-times-circle{
  cursor: pointer;
  font-size: 2rem;
}

.fa-times-circle{
  margin-left: 10px;
}

.btn-confirma-cancela{
  margin-left: 25px;
}

</style>
