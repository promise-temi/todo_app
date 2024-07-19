<template class="">
    
    <section class="section-todo-list  ">
        <span class="todos-number">{{ todosNumber }} taches</span>
                    <div class="todo-list ">
                        <select v-model="sortOrder" class="todo-select" @change="sortTodos">
                            <option value="plus-recent">Plus récents</option>
                            <option value="moins-recent">Moins récents</option>
                            <option value="importance">Importance</option>
                            <option value="complete">Complétés</option>
                                <option value="not-complete">Non complétés</option>
                            <option value="expire">Expirée</option>
                        </select>

                        <div class="todos">
                            <div class="item">
                            <TodoItem @showinfos="showinfos" v-for="todoData in todosData" v-bind:key="todoData.id"  v-bind:id="todoData.id" v-bind:titre="todoData.title" v-bind:categorie="todoData.category" v-bind:limite="todoData.due_date" date="" v-bind:importance="todoData.importance"  v-bind:description="todoData.description" v-bind:time="todoData.due_time" v-bind:isdone="todoData.done"></TodoItem>
                            </div>
                        </div>
                    </div>
                    
                    <PaginationComp v-show="todosNumber > 3" v-bind:next="nextPage" v-bind:previous="previousPage" v-bind:current_page="current_page" v-bind:page_number="page_number"></PaginationComp>
                </section>
                
               
</template>

<script>
import axios from 'axios';
import TodoItem from './TodoItem.vue'
import PaginationComp from './PaginationComp.vue'



export default {
    data() { 
    return {
        todosData: [],
        originalTodosData: [],
        todosNumber: 0,
        page_number: 0,
        current_page: 1,
        sortOrder: 'plus-recent',
    };
},
    components: {
        TodoItem,
        PaginationComp,
        
    },
    methods:{
        showinfos(todoItemData) {
      this.$emit('toggle-infos', todoItemData); // Emit an event when clicked
    },
        getTodos() {
        axios.get('http://localhost:5000/api/send_todo_back')
            .then(response => {
                this.todosData = response.data;
                this.originalTodosData = response.data;
                //for sorting
                this.sortTodos(); // Ensure data is sorted after fetching
                this.todosNumber = response.data.length;
                this.page_number = Math.ceil(this.todosData.length / 3);
            })
            .catch(error => {
                console.log('There was an error!', error);
                console.log('There was an error fetching todos!');
            });
    },
    updateSessionStorage() {
            localStorage.setItem('todoInfos', JSON.stringify(this.todosData));
            
        },
    sortTodos() {
        switch (this.sortOrder) {
            case 'plus-recent':
                this.todosData = this.originalTodosData
                this.todosData.sort((a, b) => new Date(b.creation_date) - new Date(a.creation_date));
                break;
            case 'moins-recent':
                this.todosData = this.originalTodosData
                this.todosData.sort((a, b) => new Date(a.creation_date) - new Date(b.creation_date));
                break;
            case 'importance':
                this.todosData = this.originalTodosData
                this.todosData.sort((a, b) => b.importance - a.importance);
                break;
            case 'complete':
                this.todosData = this.originalTodosData
                this.todosData = this.todosData.filter(a => a.done === 1);
                break;
            case 'not-complete':
                this.todosData = this.originalTodosData
                this.todosData = this.todosData.filter(a => a.done === 0);
                break;
            case 'expire':
                this.todosData = this.originalTodosData
                this.todosData = this.todosData.filter(a => a.expired === 1);
                break;
        }
    },
    nextPage() {
     if(this.current_page == this.page_number){
        return;
    }   
    let todos = document.querySelector('.item');
    let currentPos = parseInt(getComputedStyle(todos).bottom);
    todos.style.bottom = (currentPos + 375) + 'px';
    
    this.current_page += 1;
    },
    previousPage(){
        if(this.current_page == 1){
        return;
    }   
    let todos = document.querySelector('.item');
    let currentPos = parseInt(getComputedStyle(todos).bottom);
    todos.style.bottom = (currentPos - 375) + 'px';
    this.current_page -= 1;
    },
    roundUpIfNotInteger(value) {
    return Math.ceil(value);
    },
    
    
    
    
    },
    mounted(){
        this.getTodos()
        
    },
    watch: {
        todosData(){
            this.getTodos();
        }
    },


}
</script>

<style lang="scss" scoped>

section{
    padding: 0 !important;
}
@media screen and (max-width: 992px){
    
    
}
.todos-number{
    display: block;
    padding: 15px;
    padding-left: 25px;
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
.todo-app{
    display: flex;
    justify-content: center;
}

div.todos{
    height: 375px;
    overflow: hidden;
    position: relative;
    margin-top: 50px;
    z-index: 2;
    
}
.item{
        position: relative;
        // bottom: 375px;
    }

// section.section-todo-list::before{
//     content: ' TACHES';
//     padding: 15px;
//     padding-left: 25px;
//     padding-top: 15px;
//     font-size: 20px;
//     font-weight: bold;
//     color: white;
//     max-height: 54px;
//     border-radius: 10px;
    
//     border-bottom-left-radius: 0;
//     border-bottom-right-radius: 0;
//     display: block;
//     background-color: #282828;
//     // background-image: linear-gradient(to right, #670ED9, #670ED9, #5038ED);
    
// }

section.section-todo-list{
    margin-top: 30px;
    //margin-left: 40px;
    height: 560px;
    // max-width: 640px;
    // min-width: 450px;
    // width: 40vw;
    // max-width: 800px;
    background-color: white;
    border-radius: 10px;
    // overflow:hidden;
    
    div.todo-list{
    padding: 25px;
    padding-bottom: 0;
    select.todo-select{
        height: 20px;
        // width: 114px;
        float: right;
        margin-bottom: 25px;
    }
    .todo-select{
        background-color: #282828;
        color: white;
        border: none;
        border-radius: 5px;
        width: 200px;
        padding-left: 15px;
        font-size: 14px;
        font-weight: 600;
        cursor: pointer;
    }

    
}
}
</style>
