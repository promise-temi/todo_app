<template>
    <section class="">
      <div class="">
      <div class="create-todo " @click="emitToggleCreate">
        <p>Nouvelle tache +</p>
      </div>
      </div>
      <div class="progression-et-statut">
          <div class="progression ">
            <h3>progression</h3>
            <div class="prod-data">
            <p>{{ Math.round((TodoAll.totalDoneTasks/TodoAll.totalTasks *100)) + '%' || 0 + '%' }}</p>
            <div class="progress">
              
              <div class="progress-bar" role="progressbar" :style=" {'width': (TodoAll.totalDoneTasks/TodoAll.totalTasks *100) + '%'}" aria-valuenow="" aria-valuemin="0" aria-valuemax="100"></div>
            </div>
            </div>
          </div>
          <div class="statut">
            <div class="a-faire"><p>Taches à faire :  {{ TodoAll.totalNotDoneTasks || 0 }}</p></div>
            <div class="completes"><p>Taches complétés :  {{ TodoAll.totalDoneTasks || 0}}</p></div>
          </div>
      </div>
    </section>
    

  </template>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        TodoAll: 0,
        TodoDone: 0,
        TodoNotDone: 0
      };
    },
    
    methods: {
      emitToggleCreate() {
        this.$emit('toggle-create'); // Emit an event when clicked
      },
      // calculateTodoStats() {
      //   const todos = JSON.parse(sessionStorage.getItem('todoInfos')) || [];
      //   console.log('Todos:', todos); // Vérifiez les données
      //   this.TodoDone = todos.filter(todo => todo.done === 1).length;
      //   this.TodoNotDone = todos.filter(todo => todo.done === 0).length;
      //   this.TodoAll = todos.length;
      // }
      async getTodoDashData() {
        axios.get('http://localhost:5000/api/dash-data')
          .then(response => {
            this.TodoAll = response.data
            
          })
          .catch(error => {
            console.error('There was an error!', error);
            console.log('There was an error fetching todos!');
          });
      }
    },
    mounted() {
      this.getTodoDashData();
    },
    watch: {
     TodoAll(){
        this.getTodoDashData();
     }
    }
    
  };
  </script>
  

<style lang="scss" scoped>
.prod-data{
  display: flex;
  margin: 0 25px;
  justify-content: space-between;
  margin-top: 20px;
  p{
    margin-right: 10px;
  }
}

.progress {
  display: flex;
  height: 1rem;
  overflow: hidden;
  font-size: .75rem;
  background-color: #e9ecef;
  border-radius: 10px;
  width: 75%;
  margin-top: 4px;
}

.progress-bar {
  display: flex;
  flex-direction: column;
  justify-content: center;
  overflow: hidden;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  background-color: #007bff;
  background-image: linear-gradient(to right, #670ED9 , #D147F3);
  transition: width .6s ease;
  border-radius: 15px;
  
}
@media screen and (max-width: 992px){
  .progression{
  width: 49%;
}
.statut{
  width: 49%;
}
.progression-et-statut{
  display: flex;
  justify-content: space-between;
}


}

@media screen and (max-width: 768px){
  .progression-et-statut{
  flex-direction: column;
  .progression{
  width: 100%;
}
.statut{
  width: 100%;
}
  }

  
}









section{
    margin-top: 30px;
}
div.create-todo{
    
    height: 55px;
    background-image: linear-gradient(to right, #670ED9, #D147F3);
    color: white;
    font-weight: 500;
    border-radius: 8px;
    p{
        text-align: center;
        padding-top: 15px;
    }
}

div.progression{
    height: 120px;
    background-color: #232323;
    border-radius: 8px;
    color: white;
    margin-top: 15px;
    h3{
        padding-top: 9px;
        padding-left: 25px;
        font-size: 18px;
        font-weight: 500;
    }
}

div.statut{
    height: 120px;
    background-color: #232323;
    border-radius: 8px;
    color: white;
    font-size: 14px;
    padding-top: 35px;
    padding-left: 25px;
    margin-top: 15px;
}
</style>