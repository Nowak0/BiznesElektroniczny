<?php

namespace Symfony\Config;

require_once __DIR__.\DIRECTORY_SEPARATOR.'Prestashop'.\DIRECTORY_SEPARATOR.'AddonsConfig.php';

use Symfony\Component\Config\Definition\Exception\InvalidConfigurationException;

/**
 * This class is automatically generated to help in creating a config.
 */
class PrestashopConfig implements \Symfony\Component\Config\Builder\ConfigBuilderInterface
{
    private $addons;
    private $_usedProperties = [];

    public function addons(array $value = []): \Symfony\Config\Prestashop\AddonsConfig
    {
        if (null === $this->addons) {
            $this->_usedProperties['addons'] = true;
            $this->addons = new \Symfony\Config\Prestashop\AddonsConfig($value);
        } elseif (0 < \func_num_args()) {
            throw new InvalidConfigurationException('The node created by "addons()" has already been initialized. You cannot pass values the second time you call addons().');
        }

        return $this->addons;
    }

    public function getExtensionAlias(): string
    {
        return 'prestashop';
    }

    public function __construct(array $value = [])
    {
        if (array_key_exists('addons', $value)) {
            $this->_usedProperties['addons'] = true;
            $this->addons = new \Symfony\Config\Prestashop\AddonsConfig($value['addons']);
            unset($value['addons']);
        }

        if ([] !== $value) {
            throw new InvalidConfigurationException(sprintf('The following keys are not supported by "%s": ', __CLASS__).implode(', ', array_keys($value)));
        }
    }

    public function toArray(): array
    {
        $output = [];
        if (isset($this->_usedProperties['addons'])) {
            $output['addons'] = $this->addons->toArray();
        }

        return $output;
    }

}
