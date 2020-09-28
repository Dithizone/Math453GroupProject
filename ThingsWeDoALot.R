# This will be a script filled with all the functions
# we do over and over again, so we could just, like, 
# call `MakeHistogram(the_data)` instead of the long-
# winded `ggplot() + geom_hist() + legend()` stuff 
# all the time.

test_function <- function(testname) {
  cat("Hi! This is the test function, and your name is ", testname, "!", sep="")
}
