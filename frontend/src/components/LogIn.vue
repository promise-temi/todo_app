<template>
    <main class="login">
        <section class="log-in">
            <div class="theform">
            <h1>SE CONNECTER</h1>
            <p class="undertitle">How to i get started lorem ipsum dolor at?</p>
            <form @submit.prevent="" action="" enctype="multipart/form-data">
                <div class="icon-user">
                    <input type="email" class="input-email log-in-form-input" id="email" placeholder="Identifiant+">
                </div>
                <div class="icon-lock">
                    <input type="password" class="input-password log-in-form-input" id="password" placeholder="Mot de passe">
                </div>
                <button type="submit" class="submit-login-form" @:click="login">Connexion</button>
                <router-link to="/signin"><p>Vous n'avez pas encore de compte?</p></router-link>
                
            </form>
        </div>
        </section>
    </main>
    </template>
    <script>
    import DOMPurify from 'dompurify';
    import axios from 'axios';
    export default {
        methods:{
            login(){
                let email = document.getElementById('email').value;
                let password = document.getElementById('password').value;
                let user = {
                        email: DOMPurify.sanitize(email),
                        password: DOMPurify.sanitize(password)
                    }
                let current_user = JSON.stringify(user);
                console.log(current_user);
                axios.post('http://localhost:5000/api/login', user)
                .then((response)=>{
                    console.log(response.data);
                    console.log('Connexion réussie');
                    let user_infos = response.data[0];
                    console.log("bonjour " + user_infos.name + ' ' + user_infos.surname + ' ' + user_infos.email +' ' + user_infos.id + ' ' + user_infos.profile_picture);
                    localStorage.setItem('user', JSON.stringify(user_infos));
                    localStorage.setItem('isConnected', "true");
                    this.$router.push('/');

                    
                    
                }).catch((error)=>{
                    console.log(error);
                    alert('Mauvais identifiants');
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
    
    input.input-email{
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