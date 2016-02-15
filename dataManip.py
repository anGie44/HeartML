class Dataset(object):
  dataset_count = 0
  
  def __init__(self, dir, subdir):
    while True:
      subdirs = next(os.walk(dir))[1]
      if len(subdirs) == 1:
        dir = os.path.join(dir, subdirs[0])
      else:
        break
    
    slices = []
    for s in subdirs:
      m  = re.match("sax_(\d+)", s)
      if m is not None:
        slices.append(int(m.group(1)))
      
    slices_map = {}
    times = []
    
    
  def _filename(self, s, t):
    return os.path.join()
    
  def _read_dicom_image(self, filename):
    d = dicom.read_file(filename)
    img = d.pixel_array
    return np.array(img)
    
  def _read_all_dicom_imageS(self):
    
  def load(self):
    self._read_all_dicom_images()
