import { NgModule } from '@angular/core';
import { Numbers3Component } from './numbers3/numbers3';
import { Numbers4Component } from './numbers4/numbers4';
import { Loto6Component } from './loto6/loto6';
@NgModule({
	declarations: [Numbers3Component,
    Numbers4Component,
    Loto6Component],
	imports: [],
	exports: [Numbers3Component,
    Numbers4Component,
    Loto6Component]
})
export class ComponentsModule {}
