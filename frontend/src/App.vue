<template>
  
  <!-- <router-link to="/">Home</router-link>
      <router-link to="/signin">Sign In</router-link>
      <router-link to="/login">Login</router-link> -->
  <router-view/>

</template>
<script>
import axios from 'axios';

export default {
 
  methods: {
      connexionSetup(){
              if (sessionStorage.getItem('isConnected') === null) {
              sessionStorage.setItem('isConnected', "false");
            }
            
      },
      sendCurrentUser(){
        
              axios.get('http://localhost:5000/api/session/')
                  .then((response) => {
                  console.log(response.data);
                  localStorage.setItem('isConnected', "true");
                }).catch((error) => {
                  console.log(error);
                  console.log('non connecté');
                  localStorage.setItem('isConnected', "false");
                });

            
      }
},
  mounted(){
    this.connexionSetup(),
    this.sendCurrentUser()

  }
  }
</script>

<style lang="scss">
  *{
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;

    
}
body{
    background-color: #F0EDFF;
    // background-image: linear-gradient(120deg ,  #F0EDFF, #F0EDFF, rgba(103, 14, 217,0.3) , #F0EDFF, #F0EDFF,rgb(209, 71, 243, 0.7));
}
main{
  
    margin-left: 165px;
    margin-top: 30px;
    color:#351350;
    background-image: none;
    
}














.poppins-thin {
  font-family: "Poppins", sans-serif;
  font-weight: 100;
  font-style: normal;
}

.poppins-extralight {
  font-family: "Poppins", sans-serif;
  font-weight: 200;
  font-style: normal;
}

.poppins-light {
  font-family: "Poppins", sans-serif;
  font-weight: 300;
  font-style: normal;
}

.poppins-regular {
  font-family: "Poppins", sans-serif;
  font-weight: 400;
  font-style: normal;
}

.poppins-medium {
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-style: normal;
}

.poppins-semibold {
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  font-style: normal;
}

.poppins-bold {
  font-family: "Poppins", sans-serif;
  font-weight: 700;
  font-style: normal;
}

.poppins-extrabold {
  font-family: "Poppins", sans-serif;
  font-weight: 800;
  font-style: normal;
}

.poppins-black {
  font-family: "Poppins", sans-serif;
  font-weight: 900;
  font-style: normal;
}

.poppins-thin-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 100;
  font-style: italic;
}

.poppins-extralight-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 200;
  font-style: italic;
}

.poppins-light-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 300;
  font-style: italic;
}

.poppins-regular-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 400;
  font-style: italic;
}

.poppins-medium-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 500;
  font-style: italic;
}

.poppins-semibold-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 600;
  font-style: italic;
}

.poppins-bold-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 700;
  font-style: italic;
}

.poppins-extrabold-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 800;
  font-style: italic;
}

.poppins-black-italic {
  font-family: "Poppins", sans-serif;
  font-weight: 900;
  font-style: italic;
}


@media screen and (max-width: 992px){
  main{
    margin-left: 0;
  }
}


</style>
