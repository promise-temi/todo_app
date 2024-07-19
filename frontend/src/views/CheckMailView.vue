<template>
    <main class="login">
        <section class="log-in">
            <div class="theform">
            <h1>Comfirmer votre email</h1>
            <p class="undertitle">Un email de confirmation vous à été envoyé</p>
            <form @submit.prevent="" action="" enctype="multipart/form-data">
                <div class="icon-user">
                    <input  class="input-code log-in-form-input" id="code" placeholder="code recu">
                </div>
                
                <button type="submit" class="submit-login-form" @:click="confirm">Confirmer</button>
                <!-- <router-link to="/signin"><p>Vous n'avez pas encore de compte?</p></router-link> -->
                
            </form>
        </div>
        </section>
    </main>
    </template>
    <script>
    import axios from 'axios';
    export default {
        methods:{
            confirm(){
                let code = document.getElementById('code').value;
                
                let data = {
                    code: code
                }
                    alert('Code correct');
                    axios.post('http://localhost:5000/api/confirm-email/' , data)
                    .then((response)=>{
                        console.log(response.data);
                        alert('Email confirmé avec succès');
                        localStorage.getItem('user').verified = true;
                        this.$router.push('/');
                    }).catch((error)=>{
                        console.log(error);
                        alert('Erreur lors de la confirmation');
                    })
                
            }
        }
    }
    </script>
    <style lang="scss" scoped>
    body{
        background-image: url('./../assets/Background-log.png');
    }
    
    div.theform{
        text-align: center;
        width: 365px;
        margin-left: 105px;
        margin-top: 100px;
        p.undertitle{
            font-size: 16px;
            margin-bottom: 30px;
        }
    }
    
    form{
        width: 365px;
        h1{
            font-size: 30px;
            font-weight: 1000;
        }
        p{
        text-align: center;
        text-decoration: underline;
        font-size: 14px;
        margin-top: 10px;
    }
    }
    section.log-in{
        width: 575px;
        height: 100vh;
        background-color: white;
        position:absolute;
        right: 0;
        top:0;
        
    }
    .log-in-form-input{
        margin-bottom: 20px;
        padding-left: 50px;
        font-size: 12px;
        color: #1C1C1C;
    }
    
    input.input-name{
        width:175px;
        height: 50px;
        border:none;
        border-radius: 15px;
        background-color: #F0EDFF;
    }
    div.icon-user::before{
        content: url('./../assets/user-icon.png');
        position: absolute;
        left:127px;
        margin-top: 14px;
    }
    div.icon-user2::before{
        content: url('./../assets/user-icon.png');
        position: absolute;
        left: 318px;
        margin-top: 14px;
    }
    
    input.input-surname{
        width:175px;
        height: 50px;
        border:none;
        border-radius: 15px;
        background-color: #F0EDFF;
    }
    
    div.icon-lock::before{
        content: url('./../assets/lock-icon.png');
        position: absolute;
        left:127px;
        margin-top: 14px;
    }
    
    input.input-code{
        width:365px;
        height: 50px;
        border:none;
        border-radius: 15px;
        background-color: #F0EDFF;
    }
    
    input.input-password{
        width:365px;
        height: 50px;
        border:none;
        border-radius: 15px;
        background-color: #F0EDFF;
    }
    
    input.input-confirm-password{
        width:365px;
        height: 50px;
        border:none;
        border-radius: 15px;
        background-color: #F0EDFF;
    }
    
    div.name-and-surname{
        display: flex;
        justify-content: space-between;
    }
    
    button.submit-login-form{
        
        margin-top: 10px;
        font-weight: bold;
        font-size: 12px;
        color: white;
        background-image: linear-gradient(to right, #670ED9, #5038ED);
        height: 52px;
        width: 124px;
        border: none;
        border-radius: 16px;
        
    }
    button.submit-login-form:hover{
        cursor: pointer;
    }
    
    </style>