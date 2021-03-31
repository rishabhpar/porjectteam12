// this file contains a class to protect routes that need login verification
// to view

class Auth {
    constructor(){
        this.authenticated = false;
    }

    login(cb){
        this.authenticated = true;
        cb();
    }

    logout(cb){
        this.authenticated = false;
        cb();
    }

    isAuthenticated () {
        return this.authenticated;
    }
}

// mimics singleton pattern
export default new Auth ()