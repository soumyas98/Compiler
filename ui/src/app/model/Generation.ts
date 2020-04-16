import { Member } from './Member';

export class Generation {
    members: Member[];
    avg_fit: Number;
    fittest: Member;
    mutation_count: Number;
    crossover_count: Number;
    curr_mem: number;

    constructor(data: any) {
        this.members = [];
        data['members'].forEach(mem => {
            this.members.push(new Member(mem));
        });
        this.avg_fit = data['avg-fit'];
        this.fittest = new Member(data['fittest']);
        this.mutation_count = data['mutation-count'];
        this.crossover_count = data['crossover-count'];

        this.curr_mem = -1;
    }

    hasMoreMembers(): boolean {
        return this.curr_mem < this.members.length - 1;
    }

    moveNext(): void {
        ++this.curr_mem;
    }

    getCurrentMemberIdx(): number {
        if (this.curr_mem == -1) {
            return undefined;
        }
        return this.curr_mem;
    }

    getCurrentMember(): Member {
        if (this.curr_mem == -1) {
            return undefined;
        }
        return this.members[this.curr_mem];
    }

    reset(): void {
        this.curr_mem = -1;
    }

}