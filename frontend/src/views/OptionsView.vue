<template>
    <div class="OPTIONS">
      <SideHeader></SideHeader>
      <div class="header-et-main">
        <TopHeader></TopHeader>
        <main>
          <div class="container">
            <div class="options col">
              <h2>Options</h2>
              <div class="edit">
                <div>
                  <fieldset class="image">
                    
                    <img :src="profileImage" alt="" class="show-image" />
                    <input type="file" @change="onFileChange" class="image" />
                  </fieldset>
                  <fieldset class="infos">
                    <label for="name">Nom</label>
                    <input type="text" v-model="user_info.name" class="name" />
                    <label for="surname">Prénom</label>
                    <input type="text" v-model="user_info.surname" class="surname" />
                    <label for="email">Email</label>
                    <input type="email" v-model="user_info.email" class="email" />
                    <p>modifier mot de passe</p>
                  </fieldset>
                </div>
                <div class="buttons">
                  <button class="btn btn-danger">Supprimer mon compte</button>
                  <button class="btn btn-primary" @click="updateProfile">Enregistrer le modifications</button>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  import SideHeader from '@/components/SideHeader.vue';
  import TopHeader from '@/components/TopHeader.vue';
  
  export default {
    components: {
      SideHeader,
      TopHeader
    },
    data() {
      return {
        currentProfileImage: localStorage.getItem('profile_picture'),
        profileImage: '',
        user_info: JSON.parse(localStorage.getItem('user')),
        selectedFile: null
      };
    },
    created() {
    
      this.profileImage = `data:image/png;base64,${this.user_info.profile_picture}`;
    
  },
    methods: {
        
      onFileChange(event) {
        const file = event.target.files[0];
        this.selectedFile = file;
        this.profileImage = URL.createObjectURL(file);
      },
      updateProfile() {
        const formData = new FormData();
        formData.append('name', this.user_info.name);
        formData.append('surname', this.user_info.surname);
        formData.append('email', this.user_info.email);
        if (this.selectedFile) {
          formData.append('profile_picture', this.selectedFile);
        }
  
        axios.put('http://localhost:5000/api/update-user', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        })
          .then((response) => {
            console.log(response.data);
            console.log('Modifications enregistrées');
            // Update the session storage with new user data if needed
          })
          .catch((error) => {
            console.log(error);
            alert('Echec de l\'enregistrement des modifications');
          });
      }
    }
  };
  </script>

<style lang="scss" scoped>
 .main{
    display: flex;
    padding: 0 50px;
    
    
    
  }
  div.options{
    width: 690px;
    height: 600px;
    background-color: white;
    margin-top: 100px;
    border-radius: 8px;
    

  }
  .edit div{
    display: flex;
    
  }
  fieldset{
    border: none;
    padding: 0 20px;
    
  }
  fieldset.image{
    display: flex;
    flex-direction: column;
    
    margin-bottom: 20px;
    img{
        width: 130px;
        height: 132px;
        object-fit: cover;
    }
  }
  fieldset.infos{
    display: flex;
    flex-direction: column;
    margin-bottom: 20px;
    label{
        font-size: 12px;
        margin-bottom: 5px;
    }
    input{
        
        
        height: 50px;
        background-color: #F0EDFF;
        border: none;
        border-radius: 15px;
        margin-bottom: 15px;
        display: flex;
        flex-direction: column;
    }
  }
</style>