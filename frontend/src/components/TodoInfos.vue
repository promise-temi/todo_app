<template class="container">
    <section class="col todo-info" ref="printSection" v-if="todoItem">
        <div class="cat-del">
            <p class="categorie">{{ todoItem.categorie }}</p>
            <div>
                <p class="délai" v-show="todoItem.limite">Limite le : {{ formattedLimite }}</p>
                <p class="délai" v-show="!todoItem.limite && !todoItem.time">Aucun délai</p>
                <p class="délai" v-show="todoItem.time"><span v-show="!todoItem.limite">Limite </span>à <span v-show="!todoItem.limite">: </span>{{ todoItem.time }}</p>
            </div>
        </div>
        <div class="titre_impo">
            <h3 class="titre">{{ todoItem.titre }}</h3>
            <p class="importance" v-show="todoItem.importance === 0" style="color:#E0E0FF;">Très Basse Importance</p>
            <p class="importance" v-show="todoItem.importance === 1" style="color:#D0F0FA;">Basse Importance</p>
            <p class="importance" v-show="todoItem.importance === 2" style="color:#ABE8AB;">Importance Modérée</p>
            <p class="importance" v-show="todoItem.importance === 3" style="color:#F1FF9B;">Importance Moyenne</p>
            <p class="importance" v-show="todoItem.importance === 4" style="color:#FFBC7E;">Haute Importance</p>
            <p class="importance" v-show="todoItem.importance === 5" style="color:#FF7E7E;">Très Haute Importance</p>
            <!-- <p class="attribut">Attribué par : </p> -->

        </div>
        <pre class="description">{{ todoItem.description }}</pre>
        <div class="buttons">
            <div class="modif-suppr">
                <!-- <button class="fait">fait</button> -->
                <button class="modifier" @click="modify">Modifier</button>
                <button class="supprimer" @click="deleteTodo">Supprimer</button>
                <svg @click="printing" xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="currentColor" class="bi bi-printer-fill" viewBox="0 0 16 16">
  <path d="M5 1a2 2 0 0 0-2 2v1h10V3a2 2 0 0 0-2-2zm6 8H5a1 1 0 0 0-1 1v3a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-3a1 1 0 0 0-1-1"/>
  <path d="M0 7a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v3a2 2 0 0 1-2 2h-1v-2a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v2H2a2 2 0 0 1-2-2zm2.5 1a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1"/>
</svg>
            </div>
            <a class="retour" @click="removeInfo">Retour</a>
        </div>
    </section>
</template>
<script>
import { format } from 'date-fns';
import { fr } from 'date-fns/locale';
import axios from 'axios';


export default {
    
  props: {
    todoItem: Object
  },
  methods: {
    printing() {
        const printContents = this.$refs.printSection.innerHTML;
        const originalContents = document.body.innerHTML;
        document.body.innerHTML = printContents;
        document.querySelector('.buttons').style.display = 'none';
        window.print();
        document.body.innerHTML = originalContents;
        window.location.reload();
    },
    modify(){
        this.$emit('modifyTodo', this.todoItem);
    },
    
    removeInfo(){
        this.$emit('remove-info');
    },
    deleteTodo(){
        let toDelete = {
            id : this.todoItem.id,
            
        }
        axios.post('http://localhost:5000/api/delete_todo', toDelete)
        .then(response => {
            console.log(response.data)
            alert('Todo supprimée avec succès!')
            this.$emit('remove-info')
            this.$emit('updateTodos')
        })
        .catch(error => {
            console.log(error)
            alert(toDelete.id)
            alert('Erreur lors de la suppression de la todo')
        });
    }
  },
  computed: {
    formattedLimite() {
      if (!this.todoItem || !this.todoItem.limite) return '';
      return format(new Date(this.todoItem.limite), 'EEEE dd MMMM yyyy', { locale: fr });
    }
  }
  
};
</script>
<style lang="scss" scoped>
section.todo-info{
    border: #D1D1D1;
    position: relative;
    //margin-left: 40px;
    min-height: 560px;
    // max-width: 640px;
    // min-width: 450px;
    margin-top: 30px;
    // max-width: 800px;
    background-color: white;
    border-radius: 10px;
    // overflow:hidden;
    display: grid;
}
div.cat-del{
    display: flex;
    justify-content: space-between;
    padding: 25px;
    p.categorie{
        font-size: 14px;
        color: #BDBDBD;
    }
    p.délai{
        font-size: 14px;
        color: #1A1A1A;
        font-weight: 500;
    }
    div{
        display: flex;
        gap: 5px;
    }
}
div.titre_impo{
    padding: 30px 50px;
}

h3{
        color: #1A1A1A;
        font-size: 20px;
    }
    .importance{
        
        font-size: 14px;
        text-transform: uppercase;
    }
    pre.description{
        padding: 0 50px;
        color: #351350;
        font-size: 16px;
        line-height: 1.5;
        white-space: pre-wrap;
    }
    
    div.buttons{
        display: flex;
        justify-content: space-between;
        padding: 50px;
        align-self: end;
        
        width: 100%;
        button{font-weight: bold;
    font-size: 12px;
    color: white;
    
    height: 52px;
    width: 124px;
    border: none;
    border-radius: 16px;
    margin-left: auto;
            cursor: pointer;
        }
        button.modifier{
            background-image: linear-gradient(to right, #670ED9, #5038ED);
            margin-right: 20px;
        }
        button.supprimer{
            background-image: linear-gradient(to right, #D90E26, #7D1313)
        }
        // button.fait{
        //     background-image: linear-gradient(to right, #94db57, #588c2b);
        //     margin-right: 20px;
            
        // }

        .bi-printer-fill{
            cursor: pointer;
            margin-left: 20px;
            position: relative;
            top: 10px;
        }
        a.retour{
            color: #1A1A1A;
            font-size: 14px;
            font-weight: 500;
            text-decoration: none;
            cursor: pointer;
            margin-right: 50px;
            padding-top: 18px;
        }
        
    }

    
</style>