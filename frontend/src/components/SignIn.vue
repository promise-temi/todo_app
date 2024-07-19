<template>
    <main class="signin">
        <section class="sign-in">
            <div class="theform">
            <h1>CREER UN COMPTE</h1>
            <p class="undertitle">How to i get started lorem ipsum dolor at?</p>
            <form @:submit.prevent="" action="">
                <div class="name-and-surname">
                    <div class="icon-user">
                        <input type="text" class="input-name sign-in-form-input" id="name" placeholder="Prénom">
                    </div>
                    <div class="icon-user icon-user2">
                        <input type="text" class="input-surname sign-in-form-input" id="surname" placeholder="Nom" >
                    </div>
                </div>
                <div class="icon-user">
                    <input type="email" class="input-email sign-in-form-input" id="email" placeholder="Email">
                </div>
                <div class="icon-lock">
                    <input type="password" class="input-password sign-in-form-input" id="password" placeholder="Mot de passe">
                </div>
                <div class="icon-lock">
                    <input type="password" class="input-confirm-password sign-in-form-input" id="password2" placeholder="Confimation mot de passe">
                </div>
                <button type="submit" class="submit-signin-form" @:click="submitForm" >S'inscrire</button>
                <router-link to="/login"><p>Vous avez déja un compte?</p></router-link>
                
            </form>
        </div>
        </section>
   </main>
    </template>
    <script>
    import axios from 'axios';
    import DOMPurify from 'dompurify';
    export default {
        methods:{
            submitForm(){
                let name = document.getElementById('name').value;
                let surname = document.getElementById('surname').value;
                let email = document.getElementById('email').value;
                let password = document.getElementById('password').value;
                let password2 = document.getElementById('password2').value;
                if(password === password2){
                    let user = {
                            name: DOMPurify.sanitize(name),
                            surname: DOMPurify.sanitize(surname),
                            email: DOMPurify.sanitize(email),
                            password: DOMPurify.sanitize(password)

                        }
                    let new_user = JSON.stringify(user);
                    alert(new_user);
                    axios.post('http://localhost:5000/api/create_account', user)
                    .then((response)=>{
                        console.log(response.data);
                        alert('Compte créé avec succès');
                        this.$router.push('/login');
                        
                    }).catch((error)=>{
                        console.log(error);
                        alert('Erreur lors de la création du compte');
                    })

                }
                else{
                    alert('Les mots de passe ne correspondent pas');
                }
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
    section.sign-in{
        width: 575px;
        height: 100vh;
        background-color: white;
        position:absolute;
        right: 0;
        top:0;
        
    }
    .sign-in-form-input{
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
    
    button.submit-signin-form{
        
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
    button.submit-signin-form:hover{
        cursor: pointer;
    }
    
    </style>