#![allow(unused_variables)]
#![allow(unused_must_use)]
use std::io::{self, prelude::*};
 
fn solve<R: BufRead, W: Write>(mut input: FastInput<R>, mut w: W) {
    let n: usize = input.token();
    let mut a = vec![0usize; n];
    let mut b = vec![0usize; n];    
    for (x, y) in a.iter_mut().zip(b.iter_mut()) {
        *x = input.token();
        *y = input.token();
    }
    let mut order: Vec<_> = (0..n).collect();
    order.sort_by(|&i, &j| {
        let z1 = a[i] + b[j];
        let z2 = a[j] + b[i];
        return z2.cmp(&z1);
    });
    let mut ans = 0u64;
    for (i, &x) in order.iter().enumerate() {
        ans += a[x] as u64 * i as u64 + b[x] as u64 * (n - 1 - i) as u64;
    }
    write!(w, "{}\n", ans);
}
 
fn main() {
    let stdin = io::stdin();
    let stdout = io::stdout();
    let input = FastInput::from(stdin.lock());
    let writer = io::BufWriter::new(stdout.lock());
    solve(input, writer);
}
 
trait TokenStream<T> {
    fn token(&mut self) -> T;
}
 
struct FastInput<R> {
    stdin: R,
    pos: usize,
}
 
impl<R: BufRead> From<R> for FastInput<R> {
    fn from(r: R) -> Self {
        FastInput { stdin: r, pos: 0 }
    }
}
 
impl<R: BufRead> TokenStream<u8> for FastInput<R> {
    fn token(&mut self) -> u8 {
        loop {
            if let Ok(buf) = self.stdin.fill_buf() {
                while self.pos < buf.len() {
                    self.pos += 1;
                    if buf[self.pos - 1] > 32 {
                        return buf[self.pos - 1];
                    }
                }
                if self.pos == 0 {
                    return 0;
                }
            } else {
                return 0;
            }
            self.stdin.consume(self.pos);
            self.pos = 0;
        }
    }
}
 
impl<R: BufRead> TokenStream<Vec<u8>> for FastInput<R> {
    fn token(&mut self) -> Vec<u8> {
        let mut ans = Vec::new();
        let mut parse_token = false;
        loop {
            if let Ok(buf) = self.stdin.fill_buf() {
                if !parse_token {
                    while self.pos < buf.len() && buf[self.pos] <= 32 {
                        self.pos += 1;
                    }
                }
                while self.pos < buf.len() && buf[self.pos] > 32 {
                    parse_token = true;
                    ans.push(buf[self.pos]);
                    self.pos += 1;
                }
                if self.pos != buf.len() || self.pos == 0 {
                    return ans;
                }
            }
            self.stdin.consume(self.pos);
            self.pos = 0;
        }
    }
}
 
macro_rules! impl_token_stream {
    ($($t:ident),+) => {$(
        impl<R: BufRead> TokenStream<$t> for FastInput<R> {
           fn token(&mut self) -> $t {
                let mut ans = 0;
                let mut parse_token = false;
                loop {
                    if let Ok(buf) = self.stdin.fill_buf() {
                        if !parse_token {
                            while self.pos < buf.len() && buf[self.pos] <= 32 {
                                self.pos += 1;
                            }
                        }
                        while self.pos < buf.len() && buf[self.pos] > 32 {
                            parse_token = true;
                            ans = ans * 10 + (buf[self.pos] - b'0') as $t;
                            self.pos += 1;
                        }
                        if self.pos != buf.len() || self.pos == 0 {
                            return ans;
                        }
                    }
                    self.stdin.consume(self.pos);
                    self.pos = 0;
                }
           }
        }
    )+}
}
 
impl_token_stream!(usize);