import argparse
import os
    
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--module", type=str)
    parser.add_argument("--dsfile", type=str)
    parser.add_argument("--outfile", type=str)

    args = parser.parse_args()

    
    module = "modules.{}".format(args.module.upper())
    print("loading module: {}".format(module))
    
    problem_module = __import__(
        module,
        fromlist=[args.module.upper()]
    )

    print("done.")

    print("running module...\n{}\n\n".format("*"*80))
    with open(args.dsfile, "r") as dsf:
        with open(args.outfile, "w") as outf:
            outf.write(problem_module.main(dsf))
        

    print("\n\n{}\ndone running module, cleaning up...\n".format("*"*80))
    print("Wrote {b} bytes to: {f}\n"
          .format(
              b=os.path.getsize(args.outfile),
              f=args.outfile
          )
    )
