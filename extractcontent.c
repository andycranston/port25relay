/*
 *  @(!--#) @(#) extractcontent.c, version 005, 30-may-2020
 *
 *  extract content from simple email file
 *
 */

/****************************************************************/

/*
 *  includes
 */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

/****************************************************************/

/*
 *  defines
 */

#ifndef TRUE
#define TRUE 1
#endif

#ifndef FALSE
#define FALSE 0
#endif

#define MAX_LINE_LENGTH 8192

/****************************************************************/

/*
 *  Main
 */

int main(argc, argv)
  int   argc;
  char *argv[];
{
  int                contentflag;
  char               line[MAX_LINE_LENGTH + sizeof(char)];

  contentflag = FALSE;

  while (fgets(line, MAX_LINE_LENGTH, stdin) != NULL) {
    if (contentflag) {
      printf("%s", line);
    } else {
      if (strcmp(line, "\n") == 0) {
        contentflag = TRUE;
      }
    }
  }

  return 0;
}

/* end of file */
