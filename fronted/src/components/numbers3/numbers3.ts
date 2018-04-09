import { Component } from '@angular/core';

/**
 * Generated class for the Numbers3Component component.
 *
 * See https://angular.io/api/core/Component for more info on Angular
 * Components.
 */
@Component({
  selector: 'numbers3',
  templateUrl: 'numbers3.html'
})
export class Numbers3Component {

  text: string;

  constructor() {
    console.log('Hello Numbers3Component Component');
    this.text = 'Hello World';
  }

}
