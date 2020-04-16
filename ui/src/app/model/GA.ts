import { Generation } from './Generation';
import { BenchMark } from './BenchMark';

export class GA {
    generation_count: Number;
    population: Number;
    crossover_rate: Number;
    mutation_rate: Number;
    elite_factor: Number;
    generations: Generation[];
    benchmark: BenchMark;

    curr_gen: number;

    constructor(data: any) {
        this.curr_gen = 0;

        this.generation_count = data['generation-count'];
        this.population = data['population'];
        this.crossover_rate = data['crossover-rate'];
        this.mutation_rate = data['mutation-rate'];
        this.elite_factor = data['elite-factor'];

        this.generations = [];
        data['generations'].forEach(gen => {
            this.generations.push(new Generation(gen))
        });
        this.benchmark = new BenchMark(data['benchmark']);
    }

    hasMoreGenerations(): boolean {
        return this.curr_gen < this.generations.length;
    }

    moveNext(): void {
        if (this.generations[this.curr_gen].hasMoreMembers()) {
            this.generations[this.curr_gen].moveNext();
        } else {
            ++this.curr_gen;
        }
    }

    getCurrentGeneration(): Generation {
        if (this.hasMoreGenerations()) {
            return this.generations[this.curr_gen];
        }
        return undefined;
    }

    getCurrentGenerationIdx() {
        return this.curr_gen;
    }

    getPreviousGen(param: string): Number {
        if (this.curr_gen == 0) {
            return undefined;
        }

        switch (param) { 
            case 'AVG_FIT':
                return this.generations[this.curr_gen - 1].avg_fit;

            case 'MUTATION_COUNT':
                return this.generations[this.curr_gen - 1].mutation_count;

            case 'CROSSOVER_COUNT':
                return this.generations[this.curr_gen - 1].crossover_count;
            
            case 'FITTEST_EXEC':
                return this.generations[this.curr_gen - 1].fittest.exec_time;

            case 'FITTEST_COMP':
                return this.generations[this.curr_gen - 1].fittest.comp_time;
        }
    }

    getCurrentMemberIdx(): number {
        if (this.hasMoreGenerations()) {
            return this.generations[this.curr_gen].getCurrentMemberIdx(); 
        }
        return undefined;
    }

    getCurrentMemberExecTime(): number {
        let curr_gen = this.getCurrentGeneration();
        if (curr_gen) {
            let curr_mem = curr_gen.getCurrentMember(); 
            if (curr_mem) {
                return curr_mem.exec_time;
            }
        }
        return undefined;
    }

    getCurrentMemberCompTime(): number {
        let curr_gen = this.getCurrentGeneration();
        if (curr_gen) {
            let curr_mem = curr_gen.getCurrentMember(); 
            if (curr_mem) {
                return curr_mem.comp_time;
            }
        }
        return undefined;
    }

    reset(): void {
        this.curr_gen = 0;
        this.generations.forEach(gen => {
            gen.reset();
        });
    }

}