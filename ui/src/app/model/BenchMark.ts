import { Member } from './Member';

export class BenchMark {
    O1: Member;
    O2: Member;
    O3: Member;
    O0: Member;

    constructor(data: any) {
        this.O1 = new Member(data['O1']);
        this.O2 = new Member(data['O2']);
        this.O3 = new Member(data['O3']);
        this.O0 = new Member(data['O0']);
    }

}