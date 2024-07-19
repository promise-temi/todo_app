<template>
    <div class="home">
      <SideHeader></SideHeader>
          <div class="header-et-main">
              <TopHeader></TopHeader>
              <main>
                <div class="container-fluid">
                  <CurrentDate></CurrentDate>
                  <div class="row main">
                      <TodoList ref="myTodoList"  @toggle-infos="toggleShowInfos" class="col" v-show="isTodoListVisible" ></TodoList>
                      <CreateTodo class="col" @todolist-updated="updateTodoAfterCreate" v-show="isCreateTodoVisible"></CreateTodo>
                      <TodoInfos @removeInfo="toggleShowInfos" @updateTodos="todoGotDeleted" @modifyTodo="showEditTodo" v-show="isShowInfosVisible" :todo-item="selectedTodoItem"></TodoInfos>
                      <EditTodo :todoItem="currentTodoItem" v-show="isEditTodoVisible" ></EditTodo>
                      <DashButtons @toggle-create="toggleCreateTodo" class="col-lg-4"></DashButtons>
                      
                  </div>
  
                </div>
                
                  
              </main>
              
          </div>
          
    </div>
  </template>
  
  <script>
  // @ is an alias to /src
  import SideHeader from '@/components/SideHeader.vue';
  import TopHeader from '@/components/TopHeader.vue';
  import TodoList from '@/components/TodoList.vue';
  import DashButtons from '@/components/DashButtons.vue';
  import CurrentDate from '@/components/CurrentDate.vue'
  import CreateTodo from '@/components/CreateTodo.vue'
  import TodoInfos from '@/components/TodoInfos.vue';
  import EditTodo from '@/components/EditTodo.vue';
  export default {
    components: {
      SideHeader,
      TopHeader,
      TodoList,
      CurrentDate,
      DashButtons,
      CreateTodo,
      TodoInfos,
      EditTodo
    },
    data(){
      return{
        isCreateTodoVisible: false,
        isShowInfosVisible: false,
        isTodoListVisible: true,
        isEditTodoVisible: false,
        selectedTodoItem: null,
        currentTodoItem: null
      }
    },
    methods: {
    toggleCreateTodo() {
      if(this.isShowInfosVisible){
        this.isShowInfosVisible = !this.isShowInfosVisible;
        this.isTodoListVisible = !this.isTodoListVisible;
      }
      if(this.isEditTodoVisible){
        this.isEditTodoVisible = !this.isEditTodoVisible;
        this.isTodoListVisible = !this.isTodoListVisible;
      }
      this.isCreateTodoVisible = !this.isCreateTodoVisible;
      this.isTodoListVisible = !this.isTodoListVisible;
    },
    toggleShowInfos(todoItemData){
      this.isShowInfosVisible = !this.isShowInfosVisible;
      this.isTodoListVisible = !this.isTodoListVisible;
      this.selectedTodoItem = todoItemData;
    },
    showEditTodo(todoItemData) { // Ajoutez le paramètre todoItemData
      this.currentTodoItem = todoItemData; // Définissez currentTodoItem avec les données reçues
      this.isShowInfosVisible = false; // Modifiez l'affichage pour masquer les infos
      this.isEditTodoVisible = true; // Affichez le composant EditTodo
    },
    toEditTodoData(currentTodoData){
      this.currentTodoItem = currentTodoData;
    },
    updateTodoAfterCreate() {
        alert('Todo list updated!');
        this.$refs.myTodoList.getTodos();
        this.toggleCreateTodo();
      },
      todoGotDeleted(){
        location.reload();
      }
  }
    
  }
  </script>
  <style lang="scss">
  
  .main{
    display: flex;
    padding: 0 50px;
    padding-right: 40px;
    gap: 20px;
    
    
  }

  @media screen and (max-width: 992px) {
    .main{
      flex-direction: column-reverse;
      
    }
    
  }
  
  
  
  </style>