<template class="container">
    <section class="add-todo col">
        <form @:submit.prevent="" action="" class="col">
            <fieldset>
                <label for="title">Titre de la tache </label>
                <input type="text" name="title" class="add-todo-input add-todo-input-title col">
            </fieldset>
            <fieldset>
                <label for="desc">Description</label>
                <textarea name="desc" id="" class="add-todo-input-desc col"></textarea>
                <!-- <input type="text" name="desc" class="add-todo-input add-todo-input-desc col"> -->
            </fieldset>
            <div class="impo-et-categorie">
                <fieldset class="impo-fielset">
                    <label for="impo">Importance</label>
                    <input type="range" name="impo" class="add-todo-input add-todo-input-range" min="0" max="5">
                </fieldset>
                <fieldset class="categorie-fieldset">
                    <select name="Categorie" id="" class="add-todo-input add-todo-input-categorie">
                        <option value="nope">Categorie</option>
                        <option value="Travail">Travail</option>
                        <option value="Loisir">Loisir</option>
                    </select>
                </fieldset>
            </div>
            <fieldset style="display:flex; gap:50px;">
                <p v-show="showdatebutton" @:click="showdate" class="date-limite">Date limite <span>+</span></p>
                <input v-show="showdateinput" type="date" value="" class="add-todo-input add-todo-input-date">
                <p v-show="showhourbutton" @:click="showhour" class="date-limite">Ajouter une heure limite <span>+</span></p>
                <input v-show="showhourinput" type="time" value="" class="add-todo-input add-todo-input-time">
            </fieldset>
            <button class="add-todo-button" @:click="submitTodo">Ajouter</button>
            
        </form>
    </section>
</template>

<script>

import axios from 'axios';
import DOMPurify from 'dompurify';

export default {
    data() {
        return {
            showdatebutton: true,
            showdateinput: false,
            showhourbutton: true,
            showhourinput: false,
            //   todos_json : this.getTodos()
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

        submitTodo() {
            let title = document.querySelector('.add-todo-input-title').value;
            let desc = document.querySelector('.add-todo-input-desc').value;
            let impo = document.querySelector('.add-todo-input-range').value;
            let categorie = document.querySelector('.add-todo-input-categorie').value;
            let date = document.querySelector('.add-todo-input-date').value;
            let time = document.querySelector('.add-todo-input-time').value;

            // let text = title +" "+ desc +" "+ impo +" "+ categorie +" "+ date;
            let todo = {
                titre: DOMPurify.sanitize(title),
                desc: DOMPurify.sanitize(desc),
                importance: DOMPurify.sanitize(impo),
                categorie: DOMPurify.sanitize(categorie),
                date: DOMPurify.sanitize(date),
                time: DOMPurify.sanitize(time)
            }
            let Newtodo = JSON.stringify(todo);
            alert(Newtodo);


            axios.post('http://localhost:5000/api/todos/', todo)
                .then(response => {
                    console.log(response.data);
                    console.log('Todo Added Successfully');
                    this.$emit('todolist-updated');
                    // this.getTodos();
                    // location.reload();
                })
                .catch(error => {
                    console.error('There was an error!', error);
                    alert('Une erreur s\'est produite!');
                });

        }
        ,

        //     getTodos(){
        //     axios.get('http://localhost:5000/api/send_todo_back')
        //     .then(response => {
        //         console.log(response.data);
        //         let output_data = response.data;
        //         return output_data
        //   })
        //     .catch(error => {
        //         console.error('There was an error!', error);
        //         alert('There was an error!');
        //   });
        //     }
    }
}


</script>

<style lang="scss" scoped>
section.add-todo::before {
    content: 'Ajouter une tache +';
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
    width: 40vw;

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