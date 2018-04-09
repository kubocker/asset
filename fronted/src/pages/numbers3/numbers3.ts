import { Component } from '@angular/core';
import { IonicPage, NavController, NavParams } from 'ionic-angular';

import {
  Numbers3Component
} from '../../components/numbers3/numbers3'

/**
 * Generated class for the Numbers3Page page.
 *
 * See https://ionicframework.com/docs/components/#navigation for more info on
 * Ionic pages and navigation.
 */

@IonicPage()
@Component({
  selector: 'page-numbers3',
  templateUrl: 'numbers3.html',
})
export class Numbers3Page {

  constructor(public navCtrl: NavController, public navParams: NavParams) {
  }

  ionViewDidLoad() {
    console.log('ionViewDidLoad Numbers3Page');
  }

}
