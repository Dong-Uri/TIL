class UserSolution {
    public final static int N = 4;

    public void doUserImplementation(int guess[]) {
        // Implement a user's implementation function
        //
        // The array of guess[] is a return array that
        // is your guess for what digits[] would be.
    	
        Solution solution = new Solution();
        Solution.Result result = new Solution.Result();
        int[][] guess_lst = new int[210][4];
        int[][] guess_ord = new int[24][4];
        boolean[][] drop_point = new boolean[10][4];
        
        int i = 0;
        int j = 0;
        
        for (int i1 = 0; i1 < 10; i1++){
            for (int i2 = i1 + 1; i2 < 10; i2++){
                for (int i3 = i2 + 1; i3 < 10; i3++){
                    for (int i4 = i3 + 1; i4 < 10; i4++){
                        guess_lst[i][0] = i1;
                        guess_lst[i][1] = i2;
                        guess_lst[i][2] = i3;
                        guess_lst[i][3] = i4;
                        i++;
                    }
                }
            }
        }
        
        i = 0;
        for (int i1 = 0; i1 < 4; i1++){
        	for (int i2 = 0; i2 < 4; i2++){
        		if (i2 == i1) {
        			continue;
        		}
        		for (int i3 = 0; i3 < 4; i3++){
        			if (i3 == i2 || i3 == i1) {
        				continue;
        			}
        			for (int i4 = 0; i4 < 4; i4++){
        				if (i4 == i3 || i4 == i2 || i4 == i1) {
        					continue;
        				}
        				guess_ord[i][0] = i1;
        				guess_ord[i][1] = i2;
        				guess_ord[i][2] = i3;
        				guess_ord[i][3] = i4;
        				i++;
        			}
        		}
        	}
        }
        
        for (i = 0; i < 10; i++) {
        	for (j = 0; j < 4; j++) {
        		drop_point[i][j] = false;
        	}
        }
        
        int trial = 0;
        int[][] results = new int[210][6];
        
        guess[0] = guess_lst[0][0];
        guess[1] = guess_lst[0][1];
        guess[2] = guess_lst[0][2];
        guess[3] = guess_lst[0][3];
        result = solution.query(guess);
        results[trial][0] = guess[0];
        results[trial][1] = guess[1];
        results[trial][2] = guess[2];
        results[trial][3] = guess[3];
        results[trial][4] = result.strike;
        results[trial][5] = result.strike + result.ball;
        if (result.strike == 0) {
        	drop_point[guess[0]][0] = true;
        	drop_point[guess[1]][1] = true;
        	drop_point[guess[2]][2] = true;
        	drop_point[guess[3]][3] = true;
        }
        trial++;
//        System.out.printf("시도횟수 %d", trial);
//        System.out.print("\n");
//        System.out.print(results[trial-1][4]);
//        System.out.print("\n");
//        System.out.print(results[trial-1][5]);
//        System.out.print("\n");
//        System.out.print(results[trial-1][0]);
//        System.out.print(results[trial-1][1]);
//        System.out.print(results[trial-1][2]);
//        System.out.print(results[trial-1][3]);
//        System.out.print("\n");
        int match_s = 0;
        int match_sb = 0;
        boolean need_chk = true;
        for (i = 1; i < 210; i++) {
        	if (results[trial-1][5] == 4) {
        		break;
        	}
        	need_chk = false;
        	for (j = 0; j < trial; j++) {
        		match_sb = 0;
        		if (guess_lst[i][0] == results[j][0] || guess_lst[i][0] == results[j][1] || guess_lst[i][0] == results[j][2] || guess_lst[i][0] == results[j][3]) {   			
        			match_sb++;
        		}
        		if (guess_lst[i][1] == results[j][0] || guess_lst[i][1] == results[j][1] || guess_lst[i][1] == results[j][2] || guess_lst[i][1] == results[j][3]) {   			
        			match_sb++;
        		}
        		if (guess_lst[i][2] == results[j][0] || guess_lst[i][2] == results[j][1] || guess_lst[i][2] == results[j][2] || guess_lst[i][2] == results[j][3]) {   			
        			match_sb++;
        		}
        		if (guess_lst[i][3] == results[j][0] || guess_lst[i][3] == results[j][1] || guess_lst[i][3] == results[j][2] || guess_lst[i][3] == results[j][3]) {   			
        			match_sb++;
        		}
        		System.out.printf("%d%d%d%d의 결과 %d와 %d\n", guess_lst[i][0], guess_lst[i][1], guess_lst[i][2], guess_lst[i][3], match_sb, results[j][5]);
        		if (match_sb != results[j][5]) {
        			break;
        		}
    			for (int k = 0; k < 24; k++) {
    				match_s = 0;
    				if (guess_lst[i][0] == results[j][guess_ord[k][0]]) {
    					match_s++;
    				}
    				if (guess_lst[i][1] == results[j][guess_ord[k][1]]) {
    					match_s++;
    				}
    				if (guess_lst[i][2] == results[j][guess_ord[k][2]]) {
    					match_s++;
    				}
    				if (guess_lst[i][3] == results[j][guess_ord[k][3]]) {
    					match_s++;
    				}
    				if (match_s == results[j][4]) {
    					need_chk = true;
    					break;
    				}
    			}
        	}
        	if (need_chk) {
        		guess[0] = guess_lst[i][0];
                guess[1] = guess_lst[i][1];
                guess[2] = guess_lst[i][2];
                guess[3] = guess_lst[i][3];
                result = solution.query(guess);
                results[trial][0] = guess[0];
                results[trial][1] = guess[1];
                results[trial][2] = guess[2];
                results[trial][3] = guess[3];
                results[trial][4] = result.strike;
                results[trial][5] = result.strike + result.ball;
                trial++;
                if (result.strike == 0) {
                	drop_point[guess[0]][0] = true;
                	drop_point[guess[1]][1] = true;
                	drop_point[guess[2]][2] = true;
                	drop_point[guess[3]][3] = true;
                }
                System.out.printf("시도횟수 %d", trial);
                System.out.print("\n");
                System.out.print(results[trial-1][4]);
                System.out.print("\n");
                System.out.print(results[trial-1][5]);
                System.out.print("\n");
                System.out.print(results[trial-1][0]);
                System.out.print(results[trial-1][1]);
                System.out.print(results[trial-1][2]);
                System.out.print(results[trial-1][3]);
                System.out.print("\n");
        	}
        }
        
//        for (int a = 80; a < 100; a++) {
//        	for (int b = 0; b < 4; b++) {
//        		System.out.print(guess_lst[a][b]);
//        	}
//        	System.out.print("\n");
//        }
        
//        guess[0] = 0;
//        guess[1] = 1;
//        guess[2] = 2;
//        guess[3] = 3;
//        result = solution.query(guess);
//        System.out.printf("S: %d\n", result.strike);
//        System.out.printf("B: %d\n", result.ball);
    }
}
