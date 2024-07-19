<template class="container">
    <section class="add-todo col">
        <form @submit.prevent="EditTodo" action="" class="col">
            <fieldset>
                <label for="title">Titre de la tâche</label>
                <input type="text" name="title" class="add-todo-input add-todo-input-title col" v-model="localTodoItem.titre">
            </fieldset>
            <fieldset>
                <label for="desc">Description</label>
                <textarea name="desc" id="" class="add-todo-input-desc col" v-model="localTodoItem.description"></textarea>
            </fieldset>
            <div class="impo-et-categorie">
                <fieldset class="impo-fielset">
                    <label for="impo">Importance</label>
                    <input type="range" name="impo" class="add-todo-input add-todo-input-range" min="0" max="5" v-model="localTodoItem.importance">
                </fieldset>
                <fieldset class="categorie-fieldset">
                    <select name="Categorie" id="" class="add-todo-input add-todo-input-categorie" v-model="localTodoItem.categorie">
                        <option value="">Categorie</option>
                        <option value="Travail">Travail</option>
                        <option value="Loisir">Loisir</option>
                    </select>
                </fieldset>
            </div>
            <fieldset style="display:flex; gap:50px;">
                <div v-show="localTodoItem.limite">
                    <p v-show="showdatebutton" @click="showdate" class="date-limite">{{localTodoItem.limite}} <span>modifier</span></p>
                    <input v-show="showdateinput" type="date" class="add-todo-input add-todo-input-date" v-model="localTodoItem.limite">
                </div>
                
                <div v-show="localTodoItem.time">
                    <p v-show="showhourbutton" @click="showhour" class="date-limite">{{localTodoItem.time}} <span>modifier</span></p>
                    <input v-show="showhourinput" type="time" class="add-todo-input add-todo-input-time" v-model="localTodoItem.time">
                </div>  

                <div v-show="!localTodoItem.limite">
                    <p v-show="showdatebutton" @click="showdate" class="date-limite">Date limite <span>+</span></p>
                    <input v-show="showdateinput" type="date" class="add-todo-input add-todo-input-date" v-model="localTodoItem.limite">
                </div>    
                <div v-show="!localTodoItem.time">
                    <p v-show="showhourbutton" @click="showhour" class="date-limite">Ajouter une heure limite <span>+</span></p>
                    <input v-show="showhourinput" type="time" class="add-todo-input add-todo-input-time" v-model="localTodoItem.time">
                </div>    
            </fieldset>
            <button class="add-todo-button" type="submit">Modifier</button>
        </form>
    </section>
</template>

<script>
import axios from 'axios';

export default {
  props: {
    todoItem: {
      type: Object,
      required: true
    }
  },
  data() {
    return {
      showdatebutton: true,
      showdateinput: false,
      showhourbutton: true,
      showhourinput: false,
      localTodoItem: { ...this.todoItem }
    }
  },
  watch: {
    todoItem: {
      handler(newVal) {
        this.localTodoItem = { ...newVal };
      },
      deep: true,
      immediate: true
    }
  },
  methods: {
    showdate() {
      this.showdateinput = true;
      this.showdatebutton = !this.showdatebutton;
    },
    showhour() {
      this.showhourinput = true;
      this.showhourbutton = !this.showhourbutton;
    },
    async EditTodo() {
      // Utilisation directe de localTodoItem pour obtenir les valeurs actuelles
      const todo = {
        id: this.localTodoItem.id,
        titre: this.localTodoItem.titre,
        desc: this.localTodoItem.description,
        importance: this.localTodoItem.importance,
        categorie: this.localTodoItem.categorie,
        date: this.localTodoItem.limite,
        time: this.localTodoItem.time
      };

        await axios.put('http://localhost:5000/api/editTodo', todo)
        .then(response => {
          console.log(response.data);
          alert('Modifié avec succès!');
          this.$emit('todolist-updated');
          location.reload();
        })
        .catch(error => {
          console.error('There was an error!', error);
          alert('There was an error!');
        });
    }
  }
}
</script>


<style lang="scss" scoped>
section.add-todo::before {
    content: 'Modifier la tache';
    padding: 15px;
    padding-left: 25px;
    padding-top: 15px;
    font-size: 20px;
    font-weight: bold;
    color: white;
    max-height: 54px;
    border-radius: 10px;

    border-bottom-left-radius: 0;
    border-bottom-right-radius: 0;
    display: block;
    background-color: #282828;
    // background-image: linear-gradient(to right, #670ED9, #670ED9, #5038ED);

}


section.add-todo {
    // max-width: 800px;
    margin-top: 30px;
    //margin-left: 40px;

    // max-width: 640px;
    // min-width: 450px;
    // width: 40vw;

    height: 480px;
    background-color: white;
    border-radius: 8px;
    padding: 0;
    

    // @media(max-width: 1300px){
    //     width: 90%;
    //     margin-left: auto;
    //     margin-right: auto;
    // }

    // margin-left: 80px;
    form {
        display: flex;
        flex-direction: column;
        padding-top: 20px;
        padding-left: 25px;
        padding-right: 25px;

        label {
            font-size: 12px;
        }
    }

    input.add-todo-input-title {
        // width: 415px;
        height: 50px;
        background-color: #F0EDFF;
        border: none;
        border-radius: 15px;
        margin-bottom: 15px;
        display: flex;
        flex-direction: column;
    }

    .add-todo-input-desc {
        // width: 415px;
        height: 100px;
        background-color: #F0EDFF;
        border: none;
        border-radius: 15px;
        margin-bottom: 25px;
        display: flex;
        flex-direction: column;
    }

    div.impo-et-categorie {
        display: flex;
        // flex-wrap: wrap;
    }

    fieldset.impo-fielset {
        display: flex;
        flex-direction: column;
    }

    input.add-todo-input-range {
        width: 260px;
        height: 10px;
    }


    input.add-todo-input-range::-webkit-slider-runnable-track {
        height: 10px;
        /* Specified height */

        background: #3F3F3F;
        /* Grey background */
        outline: none;
        /* Remove outline */
        border-radius: 5px;
    }

    select.add-todo-input-categorie {
        height: 20px;
        width: 114px;
        margin-top: 12px;
    }

    fieldset.categorie-fieldset {
        margin-left: 42px;
    }

    p.date-limite {
        cursor: pointer;
        margin-top: 30px;
    }

}

button.add-todo-button {
    font-weight: bold;
    font-size: 12px;
    color: white;
    background-image: linear-gradient(to right, #670ED9, #5038ED);
    height: 52px;
    width: 124px;
    border: none;
    border-radius: 16px;
    margin-left: auto;
    // margin-right: 43px;
}


fieldset {
    border: none;
}


</style>