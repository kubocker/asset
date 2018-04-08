import {
    PrimaryGeneratedColumn,
    Column,
    Entity
} from "typeorm";

@Entity()
export class Loto {
    @PrimaryGeneratedColumn()
    id: number;

    @Column()
    title: string;

    @Column()
    date: string;

    @Column()
    number1: string;

    @Column()
    number2: string;

    @Column()
    number3: string;

    @Column()
    number4: string;

    @Column()
    number5: string;

    @Column()
    number6: string;

    @Column()
    calendar: string;

    @Column()
    week: string;
}
