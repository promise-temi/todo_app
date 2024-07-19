

<!-- HTML TEMPLATE -->
<template>
    <header class="top-header">
                <h1>TODO-APP</h1>
                <span @click="logout" class="material-symbols-outlined logout-icon">logout</span>
                <section class="deconnexion-confirm">
                    <div>
                        <p>Vous êtes sur le point de vous déconnecter</p>
                        <router-link to="/login"><button class="confirm-deconnexion" @click="confirme">Confirmer</button></router-link>
                        <button class="cancel-deconnexion" @click="rester">Annuler</button>
                    </div>
                    
                </section>
  </header>
</template>
<script>
import axios from 'axios';
export default {
    methods:{
        logout(){
            document.querySelector('.deconnexion-confirm').style.display = 'block';
        },
        rester(){
            document.querySelector('.deconnexion-confirm').style.display = 'none';
        },
        confirme(){
            document.querySelector('.deconnexion-confirm').style.display = 'block';
            localStorage.clear();
            localStorage.setItem('isConnected', "false"); 

            axios.post('http://localhost:5000/api/logout')
            .then((response)=>{
                console.log(response.data);
                alert('Vous êtes déconnecté');
                localStorage.setItem('isConnected', "false"); 
            }).catch((error)=>{
                console.log(error);
                alert('Une erreur est survenue lors de la déconnexion');
            })
            this.$router.push('/login');

        }
    }
}
</script>


<!-- SCSS STYLESHEET -->
<style lang="scss">

section.deconnexion-confirm{
    display: none;
    position: fixed;
    top: 50px;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    z-index: 10;
    
    div{
        width: 300px;
        height: 200px;
        background-color: white;
        margin: 0 auto;
        margin-top: 200px;
        text-align: center;
        padding-top: 15px;
        border-radius: 15px;
        
        p{
            font-size: 18px;
            
        }
        button{
            
            width: 100px;
            height: 30px;
            border: none;
            background-color: #351350;
            color: white;
            cursor: pointer;
            margin: auto 5px;
            margin-top: 50px;
            border-radius: 5px;
        }
    }
}

header.top-header{
    background-color: white;
    height: 50px;
    position: fixed;
    top: 0px;
    display: block;
    width: 100%;
    display: flex;
    justify-content: space-between;
    z-index: 9;
    h1{
        margin-left: 165px;
        padding-left: 30px;
        padding-top: 12px;
        font-size: 18px;
        font-weight: bold;
    }
    .logout-icon{
        margin-top: 12px;
        margin-right: 25px;
        cursor: pointer;
    }
}

</style>
