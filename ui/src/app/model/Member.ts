export class Member {
    exec_time: number;
    comp_time: number;
    exec_file: string;

    constructor(data: any) {
        this.exec_time = data['exec-time'];
        this.comp_time = data['comp-time'];
        this.exec_file = data['exec-file'];
    }
}