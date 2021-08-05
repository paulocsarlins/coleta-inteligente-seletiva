<template>
  <div>
    <nav class="menu-breadcrumb animate__animated animate__fadeIn">
      <div class="nav-wrapper">
        <div class="col s12">
          
          <a href="#!" class="breadcrumb">Início</a>
          <a href="#!" class="breadcrumb">Denúncias</a>
          <a href="#!" class="breadcrumb">Cadastro de denúncias</a>
 
        </div>
      </div>
    </nav>

    <div class="content card">
      <div class="row">
        <h2 class="animate__animated animate__fadeIn">
          <i class="fas fa-bullhorn"></i>Informe o local, descreva sua denúncia e, se possível, anexe evidências.

          </h2>

        <div class="row">
          <form class="col s12">

              <div class="row">
                  <div class="input-field col s6">
                      <input placeholder="Rua, Praça, Travessa" id="first_name" type="text" class="validate" v-model="endereco">
                        <label for="first_name">Endereço</label>
                  </div>
              </div>

               <div class="row">
                  <div class="input-field col s6">
                      <input placeholder="123" id="first_name" type="text" class="validate" v-model="numero">
                        <label for="first_name">Número</label>
                  </div>
              </div>

               <div class="row">
                  <div class="input-field col s6">
                      <input placeholder="Centro" id="first_name" type="text" class="validate" v-model="bairro">
                        <label for="first_name">Bairro</label>
                  </div>
              </div>

               <div class="row">
                  <div class="input-field col s6">
                      <input placeholder="Palmares" id="first_name" type="text" class="validate" v-model="cidade">
                        <label for="first_name">Cidade</label>
                  </div>
              </div>

              <div class="row">
                  <div class="input-field col s12">
                      <textarea placeholder="Descreva sua denúncia aqui" id="textarea2" class="materialize-textarea" v-model="descricao"></textarea>
                      <label for="textarea2">Denúncia</label>
                 </div>
              </div>

              <div class="file-field input-field">
                <div class="btn">
                  <span>Carregar arquivos</span>
                  <input type="file" multiple>
                </div>
              <div class="file-path-wrapper">
                <input class="file-path validate col s6" type="text" placeholder="Fotos ou vídeos">
                </div>
              </div>
   
          </form>
    
            <button v-on:click="insertDenuncia()" class="btn waves-effect waves-light btn-denuncia" type="submit" name="action">Enviar denúncia</button>
 
        </div>
 
          </div>
        </div>
      </div>
    
  
</template>

<script>
import axios from 'axios'

export default {
  name: 'cadastro-denuncias',
  data(){
    return {
      endereco: "",
      bairro: "",
      cidade: "",
      descricao: ""
      
    }
  },

  methods: {

  insertDenuncia() {
    if(
      this.endereco == "" ||
      this.bairro == "" ||
      this.cidade == "" ||
      this.denuncia == ""
    ){
      alert('Os campos devem ser preenchidos')
    }
      axios.post('http://localhost:8000/api/adddenuncia', { endereco:this.endereco, numero:this.numero, bairro:this.bairro, cidade:this.cidade, descricao:this.descricao })
        .then(() => {
          alert('Denúncia criada com sucesso!');
          
        }).catch(error => console.log(error));
    },
  
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
  width: 50%;
  margin-left: 25%;
  padding: 1px 32px;
  margin-top: 50px;
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

.btn-denuncia{
    margin-top: 40px;
    margin-left: 40%;
}
</style>
