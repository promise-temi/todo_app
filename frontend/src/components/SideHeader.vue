<!-- VUE JAVASCRIPT -->
<script>
    export default {
        
    
    data(){
        return{
            profileImage: localStorage.getItem('profile_picture'),
            user_infos: JSON.parse(localStorage.getItem('user')),
            name: "",
            surname: "",
            email: "",
            id: "",
            profilePicture: ""
        }
    },
    methods:{
        getUserInfos(){
            if(localStorage.getItem('isConnected') === "true"){
                this.name = this.user_infos.name;
                this.surname = this.user_infos.surname;
                this.email = this.user_infos.email;
                this.id = this.user_infos.id;
                this.profilePicture = `data:image/png;base64,${this.user_infos.profile_picture}`;
                
            }
        }
    },
    mounted(){
        this.getUserInfos();
    }
}
    
</script>

<!-- HTML TEMPLATE -->
<template>
    
    <header class="sidebar">
          <div class="photo-name">
              <img v-bind:src="profilePicture" alt="">
              <h2>{{name}}<br>{{surname}}</h2>
          </div>
          <nav>
              <ul>
                  <router-link to="/" style="text-decoration: none;"><li class="todo-list">TO-DO LIST</li></router-link>
                  <router-link to="/options"><li class="options">OPTIONS<span class="material-symbols-outlined icon-settings">settings</span></li></router-link>
              </ul>
          </nav>
      </header>
     
</template>



<!-- SCSS STYLESHEET -->
<style lang="scss">

header.sidebar{
    background-color: #121212;
    color: white;
    height: 100vh;
    width: 165px;
    position: fixed;
    top: 0;
    z-index: 10;
    div.photo-name{
        height: 180px;
        border-bottom: #616161 solid 1px;
        // border-bottom: white solid 1px;
        img{
            border: solid 1px black;
            border-radius: 50%;
            height: 79px;
            width: 79px;
            background-color: white;
            margin: 0 42px;
            margin-top: 30px;
            object-fit: cover;
        }
        h2{
            font-size: 18px;
            font-weight: bold;
            text-align: center;
        }
    }
    nav{
        ul{
            
            li{
                height: 40px;
                font-size: 14px;
                font-weight: 500;
                border-bottom: #616161 solid 1px;
                // border-bottom: white solid 1px;
                padding: 9px 0;
                padding-left: 31px;
                cursor: pointer;
                color: white;
                text-decoration: none;
            }
            
            li.options{
                border-top: #616161 solid 1px;
                // border-top: white solid 1px;
                position: absolute;
                bottom: 0;
                width: 165px;
                .icon-settings{
                    color: white;
                    font-size: 20px;
                    position: relative;
                    bottom: -5px;
                    right: -8px;
                }
            }
        }
    }
  
}

@media screen and (max-width: 992px) {
    .sidebar{
        display: none;
    }
    
  }















</style>
