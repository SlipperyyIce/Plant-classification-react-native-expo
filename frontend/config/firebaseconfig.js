import { initializeApp } from "firebase/app";
import { getAuth, GoogleAuthProvider } from "firebase/auth";


const firebaseConfig = { // replace with own firebaseConfig
    apiKey: "*******************",
    authDomain: "********.firebaseapp.com",
    projectId: "********.",
    storageBucket: "********.appspot.com",
    messagingSenderId: "********",
    appId: "1:********:web:*************",
    measurementId: "*-********"
  };
  
const Firebase = initializeApp(firebaseConfig)
export const auth = getAuth(Firebase);
export default Firebase