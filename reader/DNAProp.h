#ifndef DNAPROP_H
#define DNAPROP_H

#include "pandabase.h"
#include "DNANode.h"

class EXPCL_PANDASKEL DNAProp : public DNANode
{
	PUBLISHED:
		DNAProp(string name);
		~DNAProp(void);
};

#endif
