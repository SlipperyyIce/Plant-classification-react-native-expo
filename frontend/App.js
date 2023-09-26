import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

import Profile from './components/Profile';
//import Info from './components/Info';
import Test from './components/Test';
import Login from './components/Login';
import Signup from './components/Signup';

const navigator = createStackNavigator({
  Test:Test,
  Login:Login,
  Signup:Signup,
  Profile: Profile
  //Info:Info
}, {
  initialRouteName: 'Login',
  defaultNavigationOptions: {
    title: 'Plants'
  }
});

export default createAppContainer(navigator);