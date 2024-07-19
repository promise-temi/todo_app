<template>
    <figure class="todo" @click="itemShowinfos">
        <span :class="{ 'pas-important': importance === 0, 'peu-important': importance === 1, 'un-peu-important': importance === 2, 'important': importance === 3, 'assez-important': importance === 4, 'tres-important': importance === 5 }"></span>
        <div class="todo-info" >
            <span class="categorie">{{ categorie }}</span>
            <figcaption>{{ titre }}</figcaption>
            <p class="limite" :class="{'proche': areClose, 'expired': isDateOrTimeExpired}" v-show="limite">
                Limite le : {{ formattedLimite }} 
                <span class="time"  v-if="time">à {{ stringToTime(time) }}</span>
            </p>
            
            <p class="limite limite-time" v-show="!limite && time">
                <span class="time" :class="{'proche': isCloseToTime, 'expired': timeExpired}" v-if="time">Limite à {{ stringToTime(time) }}</span>
            </p>
            <p class="delai-depasse" v-show="limite" :class="{'delai-depasse-show': isExpired}">délai dépassé</p>
            <p class="delai-depasse" v-show="time" :class="{'delai-depasse-show': timeExpired}"><span>délai dépassé</span></p>
        </div>
        <input  class="check" @click.stop="toggleIsDone" type="checkbox" :checked="isdone">
    </figure>
</template>


<script>
import axios from 'axios';
import { formatDate } from '../utils/date';

export default {
    props: ['id', 'titre', 'categorie', 'limite', 'date', 'importance', 'fait', 'description', 'time', 'isdone'],
    computed: {
        formattedLimite() {
            return this.limite ? formatDate(this.limite) : '';
        },
        isCloseToLimit() {
            return this.differenceInDays(this.limite) <= 1 && !this.isExpired;
        },
        isExpired() {
            return this.differenceInDays(this.limite) < 0 && !this.areClose;
        },
        areClose() {
            return this.differenceInDays(this.limite) < 1;
        },
        isCloseToTime() {
            const hoursDifference = this.timeDifferenceInHours();
            console.log(`Hours Difference: ${hoursDifference}`);
            return hoursDifference <= 1 && hoursDifference > 0;
        },
        timeExpired() {
            if (!this.limite) {
                const hoursDifference = this.timeDifferenceInHours();
                console.log(`Time Expired: ${hoursDifference <= 0}`);
                return hoursDifference <= 0;
            }
            return false; // Ne pas considérer le temps expiré si limite existe
        
        },
        isDateOrTimeExpired() {
            return (this.limite && this.isExpired) && (this.time && this.timeExpired);
        }
    },

    data() {
        return {
            localIsDone: this.isdone
        };
    },
    methods: {
       
        itemShowinfos() {
            this.$emit('showinfos', {
                id: this.id,
                titre: this.titre,
                categorie: this.categorie,
                limite: this.limite,
                importance: this.importance,
                fait: this.fait,
                description: this.description,
                time: this.time,
                iddone: this.localIsDone
            });
        },
        differenceInDays(taskDate) {
            const date2 = new Date(taskDate);
            const date1 = new Date();
            const Difference_In_Time = date2.getTime() - date1.getTime();
            const Difference_In_Days = Math.round(Difference_In_Time / (1000 * 3600 * 24));
            return Difference_In_Days;
        },
        stringToTime(timeString) {
            let formattedTime = timeString.match(/^\d{1,2}:\d{2}/)[0];
            return formattedTime;
        },
        timeDifferenceInHours() {
            if (!this.time) return -1;
            const limitTimeString = this.stringToTime(this.time);
            const [limitHours, limitMinutes] = limitTimeString.split(':').map(Number);
            const now = new Date();

            const limitTime = new Date(now.getFullYear(), now.getMonth(), now.getDate(), limitHours, limitMinutes);
            const timeDifference = limitTime - now;

            const hoursDifference = timeDifference / (1000 * 60 * 60);
            return hoursDifference;
        },
        
        async checking() {
            let isdone = {
            id: this.id,
            done: this.localIsDone
            }
            
             axios.put('http://localhost:5000/api/isdone', isdone)
                .then(response => {
                    console.log(response.data);
                    // alert('Todo updated successfully!');
                    this.$emit('todo-updated');
                })
                .catch(error => {
                    console.error('There was an error!', error);
                    console.log('There was an error updating todo!');
                });
        },
        toggleIsDone() {
            this.localIsDone = !this.localIsDone;
        }
    },
    watch: {
        localIsDone() {
                this.checking();
        
        }
    }
}

</script>
<style lang="scss">

.delai-depasse {
    color: black !important;
    display: none;
}
.delai-depasse-show{
    display: block;
}
.expired {
    display: none;
}

.pas-important {
    display: inline-block;
    width: 20px;
    height: 100px;
    position: absolute;
    background-color: #E0E0FF;
    border-radius: 5px;
}

.peu-important {
    display: inline-block;
    width: 20px;
    height: 100px;
    position: absolute;
    background-color: #D0F0FA;
    border-radius: 5px;
}

.un-peu-important {
    display: inline-block;
    width: 20px;
    height: 100px;
    position: absolute;
    background-color: #ABE8AB;
    border-radius: 5px;
}

.important {
    display: inline-block;
    width: 20px;
    height: 100px;
    position: absolute;
    background-color: #F1FF9B;
    border-radius: 5px;
}

.assez-important {
    display: inline-block;
    width: 20px;
    height: 100px;
    position: absolute;
    background-color: #FFBC7E;
    border-radius: 5px;
}

.tres-important {
    display: inline-block;
    width: 20px;
    height: 100px;
    position: absolute;
    background-color: #FF7E7E;
    border-radius: 5px;
}

.proche {
    color: #FF0000;
}

figure.todo {
    height: 100px;
    width: 100%;
    border: 1px solid rgba(209, 209, 209, 0.2);
    display: flex;
    margin-bottom: 25px;
    border-radius: 1px;
    border-top-left-radius: 5px;
    border-bottom-left-radius: 5px;
    cursor: pointer;


    div.todo-info {
        padding-left: 45px;
        margin-top: 10px;
        

        span.categorie {
            color: #BDBDBD;
            font-size: 12px;
        }

        figcaption {
            font-size: 16px;
            white-space: nowrap;
            margin-right: 20px;
        }

        p.limite {
            color: #939393;
            font-size: 14px;
            font-weight: 500;
        }

        p.proche {
            color: #FF0000;
            font-size: 14px;
            font-weight: 500;
        }
    }

    input {
        min-height: 30px;
        min-width: 30px;
        color: rgba(53, 19, 80, 0.65);
        margin-top: auto;
        margin-bottom: auto;
        margin-left: auto;
        margin-right: 24px;
    }
}





</style>