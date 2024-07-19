import {defineStore} from 'pinia'

export const useSessionStore = defineStore('session', {

    state: () => ({
        user: null,
        token: null,
        connected: false,
    }),
    actions: {
        checkConnected(){
            if(this.connected == false){
                this.$router.push({name: 'login'});
            }
        },
        setUser(userInfos_){
            let userInfos = JSON.stringify(userInfos_);
            sessionStorage.setItem('user_info', userInfos);
            this.user = JSON.parse(sessionStorage.getItem('user_info'))
            ;
        }

    }
})