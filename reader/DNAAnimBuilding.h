#ifndef DNAANIMBUILDING_H
#define DNAANIMBUILDING_H

#include "pandabase.h"
#include "DNALandmarkBuilding.h"

class EXPCL_PANDASKEL DNAAnimBuilding : public DNALandmarkBuilding
{
	PUBLISHED:
		DNAAnimBuilding(string name);
		~DNAAnimBuilding(void);
};

#endif
